"""
YouTube video extraction utility using yt-dlp
"""
import re
import json
from typing import Optional, List, Dict, Any
import requests
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
            "subtitle_format": "json3",
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
        Extract captions from YouTube video with timestamps.
        Downloads subtitle files from URLs provided by yt-dlp.
        
        Args:
            url: YouTube video URL
            
        Returns:
            List of CaptionSegment objects or empty list if extraction fails
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                subtitles = info.get("subtitles", {})
                auto_captions = info.get("automatic_captions", {})
                
                # Prefer manual English subtitles, then auto English, then any language
                caption_list = None
                if "en" in subtitles:
                    caption_list = subtitles["en"]
                elif "en" in auto_captions:
                    caption_list = auto_captions["en"]
                else:
                    # Try first available language
                    all_captions = {**subtitles, **auto_captions}
                    if all_captions:
                        first_lang = next(iter(all_captions.keys()))
                        caption_list = all_captions[first_lang]
                
                if not caption_list:
                    print("No caption tracks found for this video")
                    return []
                
                # Try to get json3 format first (easiest to parse), then vtt, then srv1
                caption_url = None
                caption_format = None
                for preferred_fmt in ["json3", "vtt", "srv1"]:
                    for entry in caption_list:
                        if entry.get("ext") == preferred_fmt:
                            caption_url = entry.get("url")
                            caption_format = preferred_fmt
                            break
                    if caption_url:
                        break
                
                # Fallback: just use the first available URL
                if not caption_url and caption_list:
                    caption_url = caption_list[0].get("url")
                    caption_format = caption_list[0].get("ext", "vtt")
                
                if not caption_url:
                    print("No caption URL found")
                    return []
                
                # Download the caption file
                print(f"Downloading captions (format: {caption_format})...")
                resp = requests.get(caption_url, timeout=15)
                resp.raise_for_status()
                captions_text = resp.text
                
                if not captions_text:
                    print("Empty caption response")
                    return []
                
                # Parse based on format
                if caption_format == "json3":
                    return self._parse_json3_captions(captions_text)
                elif caption_format == "srv1":
                    return self._parse_srv1_captions(captions_text)
                else:
                    return self._parse_vtt_captions(captions_text)
                
        except Exception as e:
            print(f"Error extracting captions: {str(e)}")
            return []

    @staticmethod
    def _parse_json3_captions(json_text: str) -> List[CaptionSegment]:
        """Parse json3 subtitle format from YouTube"""
        try:
            data = json.loads(json_text)
            segments = []
            events = data.get("events", [])
            
            for event in events:
                start_ms = event.get("tStartMs", 0)
                duration_ms = event.get("dDurationMs", 0)
                segs = event.get("segs", [])
                
                text_parts = []
                for seg in segs:
                    t = seg.get("utf8", "").strip()
                    if t and t != "\n":
                        text_parts.append(t)
                
                text = " ".join(text_parts).strip()
                if text:
                    segments.append(
                        CaptionSegment(
                            timestamp=start_ms / 1000.0,
                            text=text,
                            duration=duration_ms / 1000.0 if duration_ms else 1.0,
                        )
                    )
            
            return segments
        except Exception as e:
            print(f"Error parsing json3 captions: {str(e)}")
            return []

    @staticmethod
    def _parse_srv1_captions(xml_text: str) -> List[CaptionSegment]:
        """Parse srv1 (XML) subtitle format"""
        try:
            import xml.etree.ElementTree as ET
            root = ET.fromstring(xml_text)
            segments = []
            
            for text_elem in root.iter("text"):
                start = float(text_elem.get("start", 0))
                dur = float(text_elem.get("dur", 1.0))
                content = text_elem.text or ""
                content = content.strip()
                
                if content:
                    segments.append(
                        CaptionSegment(
                            timestamp=start,
                            text=content,
                            duration=dur,
                        )
                    )
            
            return segments
        except Exception as e:
            print(f"Error parsing srv1 captions: {str(e)}")
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
                    parts = line.split("-->")
                    timestamp_str = parts[0].strip()
                    end_str = parts[1].strip().split(" ")[0]  # Remove positioning info
                    start_time = YouTubeExtractor._convert_timestamp_to_seconds(timestamp_str)
                    end_time = YouTubeExtractor._convert_timestamp_to_seconds(end_str)
                    
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
                                duration=max(end_time - start_time, 1.0)
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
