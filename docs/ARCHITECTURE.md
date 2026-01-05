# Architecture & Technical Details

## System Overview

The Video Intelligence System is a full-stack web application consisting of:

1. **Backend API** - FastAPI server for video processing and AI analysis
2. **Frontend UI** - Next.js web interface for user interaction
3. **AI Engine** - LM Studio local language model integration
4. **Data Pipeline** - YouTube extraction → Caption processing → AI analysis

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     User Browser                                 │
│                  (http://localhost:3000)                         │
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │            Next.js Frontend Application                  │  │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────┐ │  │
│  │  │ Video Analyzer │  │ Video Results  │  │   Styles   │ │  │
│  │  │   Component    │  │   Component    │  │  (Tailwind)│ │  │
│  │  └────────────────┘  └────────────────┘  └────────────┘ │  │
│  │         │                                                  │  │
│  │         └─────────────────┬──────────────────────────────┘  │
│  └──────────────────────────┬───────────────────────────────────┘
│                             │
│                    HTTP POST /api/analyze
│                    (YouTube URL)
│
└────────────────────────────────────────────────────────────────┐
│                          Network Layer                         │
└────────────────────────────────────────────────────────────────┘
│
│  ┌────────────────────────────────────────────────────────────┐
│  │          FastAPI Backend (port 8000)                       │
│  │                                                             │
│  │  ┌──────────────────────────────────────────────────────┐  │
│  │  │ main.py - FastAPI Application                       │  │
│  │  │  ├─ GET /health         (health check)             │  │
│  │  │  ├─ POST /api/analyze   (main endpoint)            │  │
│  │  │  └─ GET /docs           (Swagger UI)              │  │
│  │  └──────────────────────────────────────────────────────┘  │
│  │                                                             │
│  │  ┌──────────────────────────────────────────────────────┐  │
│  │  │ YouTubeExtractor (utils/youtube_extractor.py)      │  │
│  │  │  ├─ extract_video_info()                           │  │
│  │  │  ├─ extract_captions()                             │  │
│  │  │  └─ _parse_vtt_captions()                          │  │
│  │  └──────────────────────────────────────────────────────┘  │
│  │                                                             │
│  │  ┌──────────────────────────────────────────────────────┐  │
│  │  │ AIAnalyzer (services/ai_analyzer.py)               │  │
│  │  │  ├─ generate_summary()                             │  │
│  │  │  ├─ extract_key_points()                           │  │
│  │  │  ├─ generate_timestamped_analysis()                │  │
│  │  │  └─ _send_request()                                │  │
│  │  └──────────────────────────────────────────────────────┘  │
│  │                                                             │
│  │  ┌──────────────────────────────────────────────────────┐  │
│  │  │ Pydantic Models (models.py)                         │  │
│  │  │  ├─ VideoRequest                                    │  │
│  │  │  ├─ VideoAnalysisResponse                           │  │
│  │  │  ├─ VideoMetadata                                   │  │
│  │  │  ├─ KeyPoint                                        │  │
│  │  │  ├─ TimestampedAnalysis                             │  │
│  │  │  └─ CaptionSegment                                  │  │
│  │  └──────────────────────────────────────────────────────┘  │
│  └────────────────────────────────────────────────────────────┘
│
│  ┌─────────────────┐      ┌──────────────────────┐
│  │  yt-dlp         │      │  requests library    │
│  │  (YouTube Data) │      │  (LM Studio API)     │
│  └────────┬────────┘      └──────────┬───────────┘
└───────────┼──────────────────────────┼──────────────────────────┐
            │                          │
    ┌───────▼────────┐        ┌────────▼──────────┐
    │ YouTube API    │        │  LM Studio API    │
    │ (video info,   │        │ (localhost:1234)  │
    │  captions)     │        │                   │
    │                │        │ smollm model      │
    └────────────────┘        └───────────────────┘
```

---

## Technology Stack Details

### Backend Technologies

#### FastAPI
- **Type:** Web Framework (ASGI)
- **Port:** 8000
- **Features:**
  - Automatic API documentation (Swagger/OpenAPI)
  - Built-in data validation (Pydantic)
  - Async/await support
  - CORS middleware

#### yt-dlp
- **Purpose:** Extract YouTube video information and captions
- **Features:**
  - Video metadata extraction
  - Subtitle/caption download
  - VTT format parsing
  - Supports various subtitle languages

#### LM Studio Integration
- **Model:** smollm-360m-instruct-v0.2
- **Type:** Local language model
- **API:** OpenAI-compatible `/v1/chat/completions`
- **Size:** ~500MB
- **Capabilities:**
  - Text summarization
  - Key point extraction
  - Segment analysis
  - Timestamped insights

#### Pydantic
- **Purpose:** Data validation and serialization
- **Models:**
  - Request models for API input
  - Response models for API output
  - Type safety and documentation

### Frontend Technologies

#### Next.js 14
- **Framework:** React meta-framework
- **Port:** 3000
- **Features:**
  - Server-side rendering (SSR)
  - Static site generation (SSG)
  - API routes capability
  - Built-in TypeScript support

#### TypeScript
- **Purpose:** Type-safe JavaScript
- **Benefits:**
  - Early error detection
  - Better IDE support
  - Code documentation
  - Maintainability

#### Tailwind CSS
- **Purpose:** Utility-first CSS framework
- **Features:**
  - Responsive design
  - Customizable theme
  - Small bundle size
  - Rapid development

#### React Hook Form
- **Purpose:** Efficient form management
- **Benefits:**
  - Minimal re-renders
  - Small bundle size
  - Easy validation integration

#### Zod
- **Purpose:** TypeScript-first schema validation
- **Benefits:**
  - Type inference
  - Custom validation rules
  - Error messages

---

## Data Flow

### Analysis Request Flow

1. **User Input** (Frontend)
   - User enters YouTube URL
   - Frontend validates URL format
   - User clicks "Analyze Video"

2. **API Request** (Frontend → Backend)
   ```
   POST /api/analyze
   {
     "url": "https://youtube.com/watch?v=..."
   }
   ```

3. **Video Extraction** (Backend)
   - yt-dlp fetches video metadata
   - yt-dlp downloads captions in VTT format
   - VTT parser converts to caption segments

4. **AI Analysis** (Backend)
   - Summary generation via LM Studio
   - Key points extraction via LM Studio
   - Timestamped segment analysis (5 segments)

5. **Response** (Backend → Frontend)
   ```json
   {
     "success": true,
     "metadata": {...},
     "summary": "...",
     "key_points": [...],
     "timestamped_analysis": [...],
     "captions": [...]
   }
   ```

6. **Display Results** (Frontend)
   - Render video metadata
   - Display summary
   - Show key points
   - Display timestamped segments
   - Show captions (collapsible)

---

## API Request Lifecycle

### Detailed Steps

1. **Input Validation**
   ```python
   # Pydantic validates VideoRequest
   url: str  # Must be provided
   ```

2. **URL Verification**
   ```python
   # Check if URL contains YouTube domains
   youtube_domains = ["youtube.com", "youtu.be", "m.youtube.com"]
   ```

3. **Metadata Extraction**
   ```python
   # yt-dlp.YoutubeDL extracts:
   - title
   - description
   - duration
   - view_count
   - uploader (channel)
   - upload_date
   - thumbnail
   ```

4. **Caption Extraction**
   ```python
   # yt-dlp extracts subtitles
   # Priority: English → Auto-captions → First available
   # Parse VTT format to CaptionSegment objects
   ```

5. **LM Studio Analysis**
   ```python
   # For each analysis type:
   # 1. Create prompt with captions
   # 2. Send to LM Studio /v1/chat/completions
   # 3. Parse response
   # 4. Structure into response model
   ```

6. **Response Serialization**
   ```python
   # Pydantic converts Python objects to JSON
   # Returns VideoAnalysisResponse
   ```

---

## Error Handling Strategy

### Frontend Error Handling

```typescript
try {
  const result = await analyzeVideo(url);
  if (result.success) {
    // Display results
  }
} catch (error) {
  // Show user-friendly error message
  // Log error for debugging
}
```

### Backend Error Handling

```python
# HTTPException for client errors (400, 503)
# Python exceptions caught and returned as 500

Error Scenarios:
- 400: Invalid URL, no captions, bad request
- 503: LM Studio unavailable
- 500: Unexpected server error
```

### LM Studio Error Handling

```python
# Timeout: 60 seconds per request
# Network error: Graceful fallback
# API error: Return None or partial result
```

---

## Performance Optimization

### Backend Optimizations

1. **Caption Processing**
   - Stream captions instead of loading all at once
   - Parse VTT format efficiently
   - Cache parsed captions

2. **LM Studio Requests**
   - Batch related prompts when possible
   - Use appropriate token limits
   - Implement request timeouts

3. **API Response**
   - Compress large responses
   - Use pagination if needed
   - Cache frequently accessed videos

### Frontend Optimizations

1. **Code Splitting**
   - Next.js automatic code splitting
   - Load components on demand

2. **Image Optimization**
   - Next.js Image component
   - Lazy loading for thumbnails

3. **State Management**
   - React Hook Form reduces re-renders
   - Minimal state updates

---

## Security Considerations

### Backend Security

1. **Input Validation**
   - Pydantic validates all inputs
   - URL format verification
   - Length limits on text

2. **CORS Configuration**
   - Configured to accept all origins (development)
   - Should be restricted in production
   - Allow specific domains

3. **API Rate Limiting**
   - Recommended for production
   - Use middleware like SlowAPI
   - Prevent abuse

### Frontend Security

1. **No Sensitive Data**
   - No API keys in frontend code
   - Environment variables for config
   - HTTPS only in production

2. **CSP Headers**
   - Content Security Policy
   - Prevent XSS attacks
   - Validate external resources

---

## Testing Strategy

### Backend Testing

```python
# Unit tests for:
# - YouTubeExtractor methods
# - AIAnalyzer methods
# - Model validation

# Integration tests for:
# - Full API endpoints
# - Error scenarios
# - LM Studio integration

# Test files: tests/
```

### Frontend Testing

```typescript
// Unit tests for:
// - Components rendering
// - Form validation
// - API client functions

// Integration tests for:
// - Full user workflows
// - API integration
// - Error handling

// Test files: __tests__/
```

---

## Deployment Considerations

### Development Environment
- Local machine with Python 3.11+, Node.js, LM Studio
- Hot reload enabled
- Full debugging enabled

### Production Environment

**Option 1: Cloud Deployment**
- Use cloud-based LLM (OpenAI, Claude)
- Deploy backend to AWS Lambda, Google Cloud Run, Azure Functions
- Deploy frontend to Vercel, Netlify, or similar

**Option 2: Server Deployment**
- Deploy backend to Linux server with Gunicorn/ASGI
- Deploy frontend as static build
- Use Nginx as reverse proxy
- Run LM Studio on same or separate server

**Option 3: Docker Deployment**
- Containerize backend
- Containerize frontend build
- Docker Compose for orchestration
- Include LM Studio in deployment

---

## Monitoring & Logging

### Backend Logging

```python
# Using Python logging
import logging
logger = logging.getLogger(__name__)

# Log levels:
# - INFO: General events
# - WARNING: Potential issues
# - ERROR: Errors that need attention
# - DEBUG: Detailed debugging info
```

### Frontend Logging

```typescript
// Console logging for development
// Error tracking for production (e.g., Sentry)
```

### Metrics to Monitor

- API response times
- Error rates
- LM Studio availability
- Video processing times
- YouTube API failures

---

## Future Enhancements

1. **Database Integration**
   - Store analysis results
   - User accounts and history
   - Analytics and insights

2. **Queue System**
   - Background job processing
   - Batch video analysis
   - Scheduled analysis

3. **WebSocket Support**
   - Real-time progress updates
   - Live streaming analysis
   - Collaborative features

4. **Advanced AI Features**
   - Speaker detection
   - Emotion analysis
   - Multi-language support

5. **Export Features**
   - PDF reports
   - JSON export
   - CSV export
   - Markdown export

---

**Architecture & Design Complete!** 🎉
