"""
YouTube video extraction utility using yt-dlp
"""
import re
import json
from typing import Optional, List, Dict, Any
import yt_dlp
from app.models import CaptionSegment, VideoMetadata


class YouTubeExtractor:
    """Utility class for extracting video information and captions from YouTube"""

    def __init__(self):
        """Initialize YouTube extractor"""
        self.ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitle_format": "vtt",
        }

    def extract_video_info(self, url: str) -> Optional[Dict[str, Any]]:
        """
        Extract video metadata from YouTube URL
        
        Args:
            url: YouTube video URL
            
        Returns:
            Dictionary containing video metadata or None if extraction fails
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                return {
                    "title": info.get("title", "Unknown"),
                    "description": info.get("description", ""),
                    "duration": info.get("duration", 0),
                    "views": info.get("view_count", 0),
                    "channel": info.get("uploader", "Unknown"),
                    "upload_date": info.get("upload_date"),
                    "thumbnail_url": info.get("thumbnail"),
                    "video_id": info.get("id"),
                }
        except Exception as e:
            print(f"Error extracting video info: {str(e)}")
            return None

    def extract_captions(self, url: str) -> Optional[List[CaptionSegment]]:
        """
        Extract captions from YouTube video with timestamps
        
        Args:
            url: YouTube video URL
            
        Returns:
            List of CaptionSegment objects or None if extraction fails
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                subtitles = info.get("subtitles", {})
                auto_captions = info.get("automatic_captions", {})
                
                # Prefer English subtitles
                captions_dict = None
                if "en" in subtitles:
                    captions_dict = subtitles["en"]
                elif "en" in auto_captions:
                    captions_dict = auto_captions["en"]
                else:
                    # Try first available language
                    all_captions = {**subtitles, **auto_captions}
                    if all_captions:
                        first_lang = next(iter(all_captions.keys()))
                        captions_dict = all_captions[first_lang]
                
                if not captions_dict:
                    return []
                
                # Extract VTT format captions
                caption_data = captions_dict[0] if captions_dict else None
                if not caption_data:
                    return []
                
                captions_text = caption_data.get("data", "")
                if not captions_text:
                    return []
                
                return self._parse_vtt_captions(captions_text)
                
        except Exception as e:
            print(f"Error extracting captions: {str(e)}")
            return []

    @staticmethod
    def _parse_vtt_captions(vtt_content: str) -> List[CaptionSegment]:
        """
        Parse VTT caption format
        
        Args:
            vtt_content: VTT formatted caption text
            
        Returns:
            List of CaptionSegment objects
        """
        segments = []
        lines = vtt_content.strip().split("\n")
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for timestamp line
            if "-->" in line:
                try:
                    # Parse timestamp
                    timestamp_str = line.split("-->")[0].strip()
                    start_time = YouTubeExtractor._convert_timestamp_to_seconds(timestamp_str)
                    
                    # Get caption text
                    caption_text = ""
                    i += 1
                    while i < len(lines) and lines[i].strip() and "-->" not in lines[i]:
                        text = lines[i].strip()
                        # Remove WebVTT formatting tags
                        text = re.sub(r"<[^>]+>", "", text)
                        if text:
                            caption_text += text + " "
                        i += 1
                    
                    caption_text = caption_text.strip()
                    if caption_text:
                        segments.append(
                            CaptionSegment(
                                timestamp=start_time,
                                text=caption_text,
                                duration=1.0
                            )
                        )
                    continue
                except Exception as e:
                    print(f"Error parsing caption line: {str(e)}")
            
            i += 1
        
        return segments

    @staticmethod
    def _convert_timestamp_to_seconds(timestamp: str) -> float:
        """
        Convert VTT timestamp to seconds
        
        Args:
            timestamp: Timestamp string in format HH:MM:SS.mmm
            
        Returns:
            Time in seconds as float
        """
        try:
            parts = timestamp.split(":")
            hours = float(parts[0]) if len(parts) > 2 else 0
            minutes = float(parts[-2]) if len(parts) > 1 else 0
            seconds = float(parts[-1])
            
            return hours * 3600 + minutes * 60 + seconds
        except Exception:
            return 0.0
