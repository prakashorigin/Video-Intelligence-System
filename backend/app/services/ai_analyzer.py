"""
AI analysis service using LM Studio
"""
import re
import time
from typing import Optional, List, Dict
import requests
from app.models import (
    KeyPoint,
    TimestampedAnalysis,
    CaptionSegment,
)


class AIAnalyzer:
    """Service for AI-powered analysis using LM Studio"""

    def __init__(self, lm_studio_url: str, model_name: str):
        """
        Initialize AI Analyzer
        
        Args:
            lm_studio_url: Base URL for LM Studio (e.g., http://localhost:1234)
            model_name: Model name to use for analysis
        """
        self.lm_studio_url = lm_studio_url.rstrip("/")
        self.model_name = model_name
        self.api_endpoint = f"{self.lm_studio_url}/v1/chat/completions"

    def is_available(self) -> bool:
        """Check if LM Studio is available"""
        try:
            response = requests.get(
                f"{self.lm_studio_url}/v1/models",
                timeout=5
            )
            return response.status_code == 200
        except Exception as e:
            print(f"LM Studio availability check failed: {str(e)}")
            return False

    def generate_summary(self, captions: List[CaptionSegment], title: str = "") -> Optional[str]:
        """
        Generate summary from video captions
        
        Args:
            captions: List of caption segments
            title: Video title for context
            
        Returns:
            Generated summary or None if generation fails
        """
        if not captions:
            return None

        # Combine captions
        full_text = " ".join([seg.text for seg in captions])
        
        # Truncate if too long to avoid token limits
        if len(full_text) > 8000:
            full_text = full_text[:8000] + "..."

        prompt = f"""You are a professional video content analyst. Generate a comprehensive summary of the following video content.

Video Title: {title}

Content:
{full_text}

Provide a clear, well-structured summary that:
1. Captures the main topic
2. Highlights key themes
3. Mentions important points
4. Is suitable for someone who hasn't watched the video

Summary:"""

        return self._send_request(prompt)

    def extract_key_points(self, captions: List[CaptionSegment], title: str = "") -> List[KeyPoint]:
        """
        Extract key points from video captions
        
        Args:
            captions: List of caption segments
            title: Video title for context
            
        Returns:
            List of KeyPoint objects
        """
        if not captions:
            return []

        full_text = " ".join([seg.text for seg in captions])
        
        if len(full_text) > 6000:
            full_text = full_text[:6000] + "..."

        prompt = f"""You are a professional video content analyst. Extract the key points from the following video content.

Video Title: {title}

Content:
{full_text}

Extract 5-8 important key points. Format each point on a new line starting with a number and period (1. , 2. , etc.)

Key Points:"""

        response = self._send_request(prompt)
        if not response:
            return []

        # Parse numbered points
        key_points = []
        lines = response.strip().split("\n")
        
        for line in lines:
            line = line.strip()
            # Match numbered points
            match = re.match(r"^\d+\.\s*(.+)$", line)
            if match:
                key_points.append(KeyPoint(point=match.group(1).strip()))

        return key_points[:8]  # Limit to 8 points

    def generate_timestamped_analysis(
        self, 
        captions: List[CaptionSegment],
        title: str = "",
        num_segments: int = 5
    ) -> List[TimestampedAnalysis]:
        """
        Generate timestamped analysis by dividing video into segments
        
        Args:
            captions: List of caption segments
            title: Video title
            num_segments: Number of segments to divide analysis into
            
        Returns:
            List of TimestampedAnalysis objects
        """
        if not captions:
            return []

        # Calculate total duration and segment boundaries
        total_duration = captions[-1].timestamp if captions else 0
        if total_duration == 0:
            return []

        segment_duration = total_duration / num_segments
        segments_analysis = []

        for seg_idx in range(num_segments):
            start_time = seg_idx * segment_duration
            end_time = (seg_idx + 1) * segment_duration

            # Get captions for this segment
            segment_captions = [
                cap for cap in captions
                if start_time <= cap.timestamp < end_time
            ]

            if not segment_captions:
                continue

            segment_text = " ".join([cap.text for cap in segment_captions])
            
            # Limit text length
            if len(segment_text) > 2000:
                segment_text = segment_text[:2000] + "..."

            prompt = f"""You are a professional video content analyst. Analyze this segment of video content and provide a brief summary with key insights.

Video Title: {title}
Segment: Part {seg_idx + 1} of {num_segments}

Content:
{segment_text}

Provide:
1. A brief 2-3 sentence summary of this segment
2. 2-3 key insights specific to this part

Format:
Summary: [your summary]
Insights: [bullet point list]"""

            response = self._send_request(prompt)
            
            if response:
                # Parse response
                summary = ""
                insights = []
                
                lines = response.split("\n")
                current_section = None
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("Summary:"):
                        summary = line.replace("Summary:", "").strip()
                        current_section = "summary"
                    elif line.startswith("Insights:"):
                        current_section = "insights"
                    elif current_section == "insights" and line.startswith("-"):
                        insight = line.lstrip("- ").strip()
                        if insight:
                            insights.append(insight)
                
                if summary:
                    segments_analysis.append(
                        TimestampedAnalysis(
                            segment_number=seg_idx + 1,
                            timestamp=start_time,
                            duration=segment_duration,
                            summary=summary,
                            key_insights=insights[:3]
                        )
                    )

        return segments_analysis

    def _send_request(self, prompt: str) -> Optional[str]:
        """
        Send request to LM Studio API
        
        Args:
            prompt: The prompt to send
            
        Returns:
            Generated response or None if request fails
        """
        try:
            payload = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 1000,
                "top_p": 0.9
            }

            response = requests.post(
                self.api_endpoint,
                json=payload,
                timeout=60
            )

            if response.status_code != 200:
                print(f"API error: {response.status_code} - {response.text}")
                return None

            response_data = response.json()
            
            # Extract the content from the response
            if "choices" in response_data and len(response_data["choices"]) > 0:
                return response_data["choices"][0]["message"]["content"].strip()

            return None

        except requests.Timeout:
            print("LM Studio API request timed out")
            return None
        except requests.RequestException as e:
            print(f"Error communicating with LM Studio: {str(e)}")
            return None
        except Exception as e:
            print(f"Error in AI analysis: {str(e)}")
            return None
