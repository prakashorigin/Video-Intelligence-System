"""
Main FastAPI application for Video Intelligence System
"""
import os
import time
from typing import Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

from app.models import (
    VideoRequest,
    VideoAnalysisResponse,
    HealthResponse,
    VideoMetadata,
    CaptionSegment,
)
from app.utils.youtube_extractor import YouTubeExtractor
from app.services.ai_analyzer import AIAnalyzer

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Video Intelligence System API",
    description="AI-powered video analysis tool for YouTube videos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234")
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "smollm-360m-instruct-v0.2")

# Initialize services
extractor = YouTubeExtractor()
ai_analyzer = AIAnalyzer(LM_STUDIO_URL, LM_STUDIO_MODEL)


@app.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Video Intelligence System API",
        "version": "1.0.0",
        "docs": "Visit /docs for interactive API documentation",
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    """Health check endpoint"""
    lm_studio_available = ai_analyzer.is_available()
    
    return HealthResponse(
        status="healthy" if lm_studio_available else "degraded",
        version="1.0.0",
        lm_studio_available=lm_studio_available,
    )


@app.post("/api/analyze", response_model=VideoAnalysisResponse, tags=["Analysis"])
def analyze_video(request: VideoRequest):
    """
    Analyze a YouTube video
    
    This endpoint:
    1. Extracts video metadata
    2. Extracts captions/subtitles
    3. Generates AI summary
    4. Extracts key points
    5. Creates timestamped analysis segments
    
    Args:
        request: VideoRequest containing YouTube URL
        
    Returns:
        VideoAnalysisResponse with complete analysis
    """
    start_time = time.time()
    
    try:
        # Validate URL
        if not request.url or not _is_valid_youtube_url(request.url):
            raise HTTPException(
                status_code=400,
                detail="Invalid YouTube URL. Please provide a valid YouTube video URL."
            )

        # Extract video information
        print(f"Extracting video info from: {request.url}")
        video_info = extractor.extract_video_info(request.url)
        
        if not video_info:
            raise HTTPException(
                status_code=400,
                detail="Failed to extract video information. Please check the URL and try again."
            )

        # Create metadata object
        metadata = VideoMetadata(
            title=video_info.get("title", "Unknown"),
            description=video_info.get("description", ""),
            duration=video_info.get("duration", 0),
            views=video_info.get("views", 0),
            channel=video_info.get("channel", "Unknown"),
            upload_date=video_info.get("upload_date"),
            thumbnail_url=video_info.get("thumbnail_url"),
        )

        # Extract captions
        print("Extracting captions...")
        captions = extractor.extract_captions(request.url)
        
        has_captions = bool(captions)

        # Check if LM Studio is available
        lm_available = ai_analyzer.is_available()
        
        summary = None
        key_points = []
        timestamped_analysis = []

        if has_captions and lm_available:
            # Full analysis with captions + AI
            print("Generating summary...")
            summary = ai_analyzer.generate_summary(captions, metadata.title)
            
            print("Extracting key points...")
            key_points = ai_analyzer.extract_key_points(captions, metadata.title)
            
            print("Generating timestamped analysis...")
            timestamped_analysis = ai_analyzer.generate_timestamped_analysis(
                captions,
                metadata.title,
                num_segments=5
            )
        elif has_captions and not lm_available:
            # Captions available but no LM Studio — provide basic text summary
            full_text = " ".join([seg.text for seg in captions[:50]])
            summary = f"[LM Studio not available — raw caption preview] {full_text[:1500]}..."
        elif not has_captions and lm_available:
            # No captions but LM Studio available — analyze from description
            desc = metadata.description or ""
            if desc:
                print("No captions found. Generating analysis from video description...")
                fake_captions = [CaptionSegment(timestamp=0, text=desc[:4000], duration=0)]
                summary = ai_analyzer.generate_summary(fake_captions, metadata.title)
                key_points = ai_analyzer.extract_key_points(fake_captions, metadata.title)
            else:
                summary = "No captions or description available for AI analysis."
        else:
            # No captions, no LM Studio
            desc = metadata.description or ""
            summary = f"[No captions found and LM Studio is not running] Video description: {desc[:1500]}" if desc else "No captions or description available."

        # Determine response message
        if has_captions and lm_available:
            message = "Video analysis completed successfully"
        elif has_captions:
            message = "Partial analysis — LM Studio is not running (captions extracted)"
        elif lm_available:
            message = "Analysis from description — no captions available for this video"
        else:
            message = "Metadata only — no captions found and LM Studio is not running"

        processing_time = time.time() - start_time

        return VideoAnalysisResponse(
            success=True,
            message=message,
            metadata=metadata,
            summary=summary,
            key_points=key_points,
            timestamped_analysis=timestamped_analysis,
            captions=captions if captions else [],
            total_segments=len(captions) if captions else 0,
            processing_time=round(processing_time, 2),
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"Error analyzing video: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing video: {str(e)}"
        )


def _is_valid_youtube_url(url: str) -> bool:
    """
    Validate if URL is a valid YouTube URL
    
    Args:
        url: URL to validate
        
    Returns:
        True if valid YouTube URL, False otherwise
    """
    youtube_domains = ["youtube.com", "youtu.be", "m.youtube.com"]
    return any(domain in url.lower() for domain in youtube_domains)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
