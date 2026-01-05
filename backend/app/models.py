"""
Pydantic models for request/response validation
"""
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class VideoRequest(BaseModel):
    """Request model for video analysis"""
    url: str = Field(..., description="YouTube video URL")


class CaptionSegment(BaseModel):
    """Single caption segment with timestamp"""
    timestamp: float = Field(..., description="Time in seconds")
    text: str = Field(..., description="Caption text")
    duration: float = Field(default=0, description="Duration of segment in seconds")


class KeyPoint(BaseModel):
    """Key point extracted from video"""
    point: str = Field(..., description="The key point")
    timestamp: Optional[float] = Field(None, description="Relevant timestamp if available")


class TimestampedAnalysis(BaseModel):
    """Analysis segment with timestamp"""
    segment_number: int = Field(..., description="Segment number")
    timestamp: float = Field(..., description="Start time in seconds")
    duration: float = Field(..., description="Duration in seconds")
    summary: str = Field(..., description="Segment summary")
    key_insights: List[str] = Field(default_factory=list, description="Key insights for this segment")


class VideoMetadata(BaseModel):
    """Video metadata information"""
    title: str = Field(..., description="Video title")
    description: str = Field(..., description="Video description")
    duration: int = Field(..., description="Duration in seconds")
    views: int = Field(default=0, description="View count")
    channel: str = Field(..., description="Channel name")
    upload_date: Optional[str] = Field(None, description="Upload date in YYYY-MM-DD format")
    thumbnail_url: Optional[str] = Field(None, description="Thumbnail URL")


class VideoAnalysisResponse(BaseModel):
    """Complete response for video analysis"""
    success: bool = Field(..., description="Whether analysis was successful")
    message: str = Field(..., description="Response message")
    metadata: Optional[VideoMetadata] = Field(None, description="Video metadata")
    summary: Optional[str] = Field(None, description="AI-generated summary")
    key_points: Optional[List[KeyPoint]] = Field(None, description="Extracted key points")
    timestamped_analysis: Optional[List[TimestampedAnalysis]] = Field(None, description="Segment-wise analysis")
    captions: Optional[List[CaptionSegment]] = Field(None, description="Full captions with timestamps")
    total_segments: Optional[int] = Field(None, description="Total number of caption segments")
    processing_time: Optional[float] = Field(None, description="Processing time in seconds")


class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Health status")
    version: str = Field(..., description="API version")
    lm_studio_available: bool = Field(..., description="LM Studio availability")
