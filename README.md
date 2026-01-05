# YouTube Video Analyzer

An intelligent video analysis tool that extracts captions, generates summaries, and provides timestamped insights from YouTube videos using AI.

## Features

- **Video Information Extraction**: Get detailed metadata (title, description, duration, views, etc.)
- **Caption Extraction**: Automatically extract and parse video captions/subtitles
- **AI-Powered Summarization**: Generate comprehensive video summaries using local LM Studio models
- **Key Points Extraction**: Identify and extract the most important concepts and takeaways
- **Timestamped Analysis**: Get detailed analysis of video segments with timestamps
- **Modern Web Interface**: Clean, responsive UI built with Next.js and shadcn/ui

## Performance

- Fast Processing: Analyzes videos with 200+ caption segments in under 30 seconds
- Cost-Effective: Uses local LM Studio models instead of expensive cloud APIs
- Efficient: Optimized to limit API calls while maintaining quality analysis
- Reliable: Robust error handling and rate limiting

## Tech Stack

**Backend**
- Python 3.11+ with FastAPI
- yt-dlp for YouTube video processing
- LM Studio for local AI analysis (smollm-360m-instruct-v0.2)
- Pydantic for data validation
- Uvicorn ASGI server

**Frontend**
- Next.js 14 with TypeScript
- shadcn/ui components
- Tailwind CSS for styling
- React Hook Form with Zod validation



## Quick Start

**Option 1: Separate Terminals (Recommended)**

Terminal 1 - Backend:
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh
```

Terminal 2 - Frontend:
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh
```

**Option 2: One-time Setup**

```bash
bash /Users/prakash/Python-program/video-intelligence-system/setup.sh
```

**Option 3: Manual Setup**

Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your LM Studio configuration
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```



## Configuration

Environment Variables

Create a .env file in the backend directory:

```
# LM Studio Configuration
LM_STUDIO_URL=http://localhost:1234
LM_STUDIO_MODEL=smollm-360m-instruct-v0.2
```

## LM Studio Setup

1. Install LM Studio from [lmstudio.ai](https://lmstudio.ai)
2. Download the smollm-360m-instruct-v0.2 model
3. Start the local server:
   - Open LM Studio
   - Load the model
   - Start the local server on port 1234
   - Ensure it's accessible at http://localhost:1234

## API Endpoints

- GET / - Root endpoint
- GET /health - Health check
- GET /docs - Interactive API documentation
- POST /api/analyze - Analyze YouTube video

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Pydantic models
│   ├── services/
│   │   └── ai_analyzer.py   # AI analysis service
│   └── utils/
│       └── youtube_extractor.py  # YouTube processing
├── requirements.txt         # Python dependencies
└── .env.example             # Environment template

frontend/
├── app/
│   ├── page.tsx            # Main page
│   ├── layout.tsx          # Root layout
│   └── globals.css         # Global styles
├── components/
│   ├── video-analyzer.tsx  # Main analyzer component
│   └── video-results.tsx   # Results display
└── lib/
    └── api.ts              # API client
```

## Usage

1. Open your browser to http://localhost:3000
2. Paste a YouTube URL in the input field
3. Click "Analyze Video"
4. View the comprehensive analysis including:
   - Video metadata
   - AI-generated summary
   - Key points
   - Timestamped analysis
   - Full captions

## Example Output

The system successfully processes videos with 200+ caption segments in under 30 seconds, generating:
- Comprehensive video summaries
- 8-9 key points
- 5 timestamped analysis segments
- Full caption extraction with timestamps

## Troubleshooting

### LM Studio Connection Error

Ensure LM Studio is running and accessible at the configured URL.

**Solution:**
1. Open LM Studio application
2. Load the model: smollm-360m-instruct-v0.2
3. Click "Start Local Server"
4. Verify the URL in .env: LM_STUDIO_URL=http://localhost:1234
5. Refresh the page

### Port Conflicts

Kill processes using the ports:

```bash
# Kill port 3000
lsof -ti:3000 | xargs kill -9 2>/dev/null

# Kill port 8000
lsof -ti:8000 | xargs kill -9 2>/dev/null
```

### Python 3.13 Issues

Use Python 3.11 or 3.12 for better compatibility.

## Development

Adding New Features:
- Backend: Modify files in backend/app/
- Frontend: Modify files in frontend/
- Test: Restart the respective services

## Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m "Add some amazing feature")
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.
