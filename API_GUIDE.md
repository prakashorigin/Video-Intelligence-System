# API Integration Guide

## Overview

The Video Intelligence System consists of a FastAPI backend and a Next.js frontend. The frontend communicates with the backend through REST API endpoints.

## Backend API

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Root Endpoint
```http
GET /
```

**Response:**
```json
{
  "message": "Welcome to Video Intelligence System API",
  "version": "1.0.0",
  "docs": "Visit /docs for interactive API documentation"
}
```

#### 2. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "lm_studio_available": true
}
```

#### 3. Video Analysis
```http
POST /api/analyze
Content-Type: application/json

{
  "url": "https://youtube.com/watch?v=dQw4w9WgXcQ"
}
```

**Success Response (200):**
```json
{
  "success": true,
  "message": "Video analysis completed successfully",
  "metadata": {
    "title": "Video Title",
    "description": "Video description...",
    "duration": 3600,
    "views": 10000,
    "channel": "Channel Name",
    "upload_date": "2024-01-01",
    "thumbnail_url": "https://..."
  },
  "summary": "Comprehensive AI-generated summary of the video...",
  "key_points": [
    {
      "point": "First key point extracted from video",
      "timestamp": null
    },
    {
      "point": "Second key point",
      "timestamp": null
    }
  ],
  "timestamped_analysis": [
    {
      "segment_number": 1,
      "timestamp": 0.0,
      "duration": 720.0,
      "summary": "Summary of this segment...",
      "key_insights": [
        "Insight 1",
        "Insight 2"
      ]
    }
  ],
  "captions": [
    {
      "timestamp": 0.0,
      "text": "Caption text",
      "duration": 5.0
    }
  ],
  "total_segments": 150,
  "processing_time": 28.5
}
```

**Error Responses:**

400 - Invalid URL:
```json
{
  "detail": "Invalid YouTube URL. Please provide a valid YouTube video URL."
}
```

400 - No Captions:
```json
{
  "detail": "No captions found for this video. Please ensure the video has available captions."
}
```

503 - LM Studio Unavailable:
```json
{
  "detail": "LM Studio service is not available. Please ensure LM Studio is running."
}
```

500 - Server Error:
```json
{
  "detail": "Error analyzing video: [specific error message]"
}
```

## Frontend API Client

Located in `frontend/lib/api.ts`

### Configuration

```typescript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
```

Set in `frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Functions

#### analyzeVideo(url: string)
```typescript
import { analyzeVideo } from '@/lib/api';

try {
  const result = await analyzeVideo('https://youtube.com/watch?v=...');
  console.log(result);
} catch (error) {
  console.error(error);
}
```

#### getHealth()
```typescript
import { getHealth } from '@/lib/api';

try {
  const status = await getHealth();
  console.log(status.lm_studio_available);
} catch (error) {
  console.error(error);
}
```

## CORS Configuration

The backend is configured to accept requests from any origin:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For production, restrict to specific origins:
```python
allow_origins=["https://yourdomain.com"],
```

## Error Handling

### Frontend Error Handling

```typescript
try {
  const result = await analyzeVideo(url);
  if (result.success) {
    // Handle success
  } else {
    // Handle failure
    console.error(result.message);
  }
} catch (error: any) {
  const errorMessage = error.detail || error.message || 'Unknown error';
  // Display error to user
}
```

### Backend Error Handling

All errors are returned as JSON with HTTP status codes:
- 400: Bad Request (invalid URL, missing captions)
- 500: Internal Server Error (processing failed)
- 503: Service Unavailable (LM Studio not running)

## Timeout Configuration

- **Backend Request Timeout:** 60 seconds
- **API Endpoint Timeout:** 60 seconds
- **Maximum Processing Time:** ~40 seconds for typical videos

## Data Models

### VideoRequest
```python
{
  "url": str  # YouTube video URL (required)
}
```

### VideoAnalysisResponse
```python
{
  "success": bool,
  "message": str,
  "metadata": VideoMetadata,
  "summary": Optional[str],
  "key_points": Optional[List[KeyPoint]],
  "timestamped_analysis": Optional[List[TimestampedAnalysis]],
  "captions": Optional[List[CaptionSegment]],
  "total_segments": Optional[int],
  "processing_time": Optional[float]
}
```

### VideoMetadata
```python
{
  "title": str,
  "description": str,
  "duration": int,  # seconds
  "views": int,
  "channel": str,
  "upload_date": Optional[str],  # YYYY-MM-DD
  "thumbnail_url": Optional[str]
}
```

### KeyPoint
```python
{
  "point": str,
  "timestamp": Optional[float]
}
```

### TimestampedAnalysis
```python
{
  "segment_number": int,
  "timestamp": float,  # seconds
  "duration": float,   # seconds
  "summary": str,
  "key_insights": List[str]
}
```

### CaptionSegment
```python
{
  "timestamp": float,
  "text": str,
  "duration": float
}
```

## Testing API Endpoints

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Analyze video
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"url": "https://youtube.com/watch?v=..."}'
```

### Using Postman

1. Create new POST request
2. URL: `http://localhost:8000/api/analyze`
3. Headers: `Content-Type: application/json`
4. Body (JSON):
```json
{
  "url": "https://youtube.com/watch?v=dQw4w9WgXcQ"
}
```

### Using Swagger UI

Visit: `http://localhost:8000/docs`

- Interactive API documentation
- Try-it-out functionality
- Real-time testing

---

For more information, see the main [README.md](README.md)
