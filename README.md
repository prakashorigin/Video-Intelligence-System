# YouTube Video Analyzer

An intelligent video analysis tool that extracts captions, generates summaries, and provides timestamped insights from YouTube videos using AI.

## ✨ Features

- **Video Information Extraction** - Get detailed metadata (title, description, duration, views, etc.)
- **Caption Extraction** - Automatically extract and parse video captions/subtitles with timestamps
- **AI-Powered Summarization** - Generate comprehensive summaries using local LM Studio models
- **Key Points Extraction** - Identify and extract the most important concepts and takeaways
- **Timestamped Analysis** - Get detailed analysis of video segments with timestamps
- **Modern Web Interface** - Clean, responsive UI built with Next.js and Tailwind CSS

## 🚀 Performance

- **Fast Processing** - Analyzes videos with 200+ caption segments in under 30 seconds
- **Cost-Effective** - Uses local LM Studio models instead of expensive cloud APIs
- **Efficient** - Optimized to limit API calls while maintaining quality analysis
- **Reliable** - Robust error handling and rate limiting

## 🧰 Tech Stack

**Backend**
- Python 3.11+ with FastAPI
- yt-dlp for YouTube video processing
- LM Studio for local AI analysis (smollm-360m-instruct-v0.2)
- Pydantic for data validation
- Uvicorn ASGI server

**Frontend**
- Next.js 14 with TypeScript
- Tailwind CSS for styling
- React Hook Form with Zod validation
- Axios for API client

## 📁 Project Structure

```
video-intelligence-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI application
│   │   ├── models.py               # Pydantic models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── ai_analyzer.py      # AI analysis service
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── youtube_extractor.py # YouTube processing
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Environment template
│   └── venv/                       # Virtual environment
├── frontend/
│   ├── app/
│   │   ├── globals.css             # Global styles
│   │   ├── layout.tsx              # Root layout
│   │   └── page.tsx                # Main page
│   ├── components/
│   │   ├── video-analyzer.tsx      # Main analyzer component
│   │   └── video-results.tsx       # Results display
│   ├── lib/
│   │   └── api.ts                  # API client
│   ├── package.json                # npm dependencies
│   ├── tsconfig.json               # TypeScript config
│   ├── tailwind.config.ts          # Tailwind config
│   └── next.config.js              # Next.js config
├── docs/
│   ├── API_GUIDE.md                # API endpoint documentation
│   ├── ARCHITECTURE.md             # System architecture
│   ├── FIXED_LOCALHOST_ISSUE.md    # Troubleshooting guide
│   ├── INSTALLATION.md             # Installation instructions
│   ├── SETUP_AND_RUN.md            # Detailed setup guide
│   ├── COMMANDS.md                 # Command reference
│   ├── QUICKSTART.md               # Quick start guide
│   └── SYSTEM_STATUS.md            # System status report
├── start-backend.sh                # Backend startup script
├── start-frontend.sh               # Frontend startup script
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
└── LICENSE                         # MIT License
```

## ⚡ Quick Start

### Option 1: Automatic Setup

```bash
bash setup.sh
```

This runs a complete setup that:
- Creates Python virtual environment
- Installs backend dependencies
- Installs frontend dependencies
- Creates configuration files
- Initializes git repository

### Option 2: Manual Setup

**Backend Setup:**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your LM Studio configuration
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend Setup:**

```bash
cd frontend
npm install
npm run dev
```

### Option 3: Quick Start Scripts

**Terminal 1 - Backend:**
```bash
bash quick-start-backend.sh
```

Wait for: `Uvicorn running on http://0.0.0.0:8000`

**Terminal 2 - Frontend:**
```bash
bash quick-start-frontend.sh
```

Wait for: `Ready in XXXms`

## ⚙️ Configuration

### Backend Environment Variables

Create a `.env` file in the `backend` directory:

```env
# LM Studio Configuration
LM_STUDIO_URL=http://localhost:1234
LM_STUDIO_MODEL=smollm-360m-instruct-v0.2

# Optional: Timeout in seconds
LM_STUDIO_TIMEOUT=60
```

### Frontend Configuration

Create a `.env.local` file in the `frontend` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🧠 LM Studio Setup

LM Studio provides the AI models for analysis. It's required to run this system.

### Installation Steps:

1. **Download LM Studio**
   - Visit [lmstudio.ai](https://lmstudio.ai)
   - Download and install

2. **Download Model**
   - Open LM Studio
   - Search for: `smollm-360m-instruct-v0.2`
   - Click Download

3. **Start Local Server**
   - Load the model
   - Click "Start Local Server"
   - Model will run on port 1234
   - Wait for: "Server is running on http://localhost:1234"

## 🔌 API Endpoints

### Health & Info

- **GET** `/` - Root endpoint
- **GET** `/health` - Health check (includes LM Studio status)

### Analysis

- **POST** `/api/analyze` - Analyze a YouTube video

  **Request Body:**
  ```json
  {
    "url": "https://youtube.com/watch?v=..."
  }
  ```

  **Response:**
  ```json
  {
    "success": true,
    "message": "Video analysis completed successfully",
    "metadata": {
      "title": "Video Title",
      "description": "...",
      "duration": 3600,
      "views": 10000,
      "channel": "Channel Name",
      "upload_date": "2024-01-01",
      "thumbnail_url": "https://..."
    },
    "summary": "AI-generated comprehensive summary...",
    "key_points": [
      {"point": "Key point 1"},
      {"point": "Key point 2"}
    ],
    "timestamped_analysis": [
      {
        "segment_number": 1,
        "timestamp": 0,
        "duration": 720,
        "summary": "Segment summary...",
        "key_insights": ["Insight 1", "Insight 2"]
      }
    ],
    "captions": [
      {
        "timestamp": 0,
        "text": "Caption text...",
        "duration": 5.0
      }
    ],
    "total_segments": 150,
    "processing_time": 28.5
  }
  ```

### Interactive API Documentation

Visit `http://localhost:8000/docs` for:
- Swagger UI documentation
- Try-it-out functionality
- Request/response examples

## 📖 Usage

1. **Open Browser**
   - Navigate to `http://localhost:3000`

2. **Enter YouTube URL**
   - Paste a valid YouTube video URL
   - Supported formats:
     - `https://youtube.com/watch?v=...`
     - `https://youtu.be/...`
     - `https://m.youtube.com/watch?v=...`

3. **Click "Analyze Video"**
   - Processing time: 20-40 seconds depending on video length

4. **View Results**
   - **Video Information** - Metadata (title, channel, duration, views)
   - **Summary** - AI-generated comprehensive summary
   - **Key Points** - 5-8 important takeaways
   - **Timestamped Analysis** - 5 segments with summaries and insights
   - **Captions** - Full caption text with timestamps (copyable)

## 📊 Example Analysis

For a 1-hour technical tutorial:

**Input:** YouTube video URL

**Output includes:**
- Video title, channel, duration, views
- Comprehensive summary (200-300 words)
- 7-8 key points
- 5 timestamped segments with insights
- 150+ caption segments with timestamps

**Processing time:** ~25-35 seconds

## 🛠️ Troubleshooting

### LM Studio Connection Error

```
Error: LM Studio service is not available
```

**Solution:**
1. Open LM Studio application
2. Load the model: `smollm-360m-instruct-v0.2`
3. Click "Start Local Server"
4. Verify URL in `.env`: `LM_STUDIO_URL=http://localhost:1234`
5. Refresh the web page

### Port Already in Use

**Backend (Port 8000):**
```bash
lsof -ti:8000 | xargs kill -9
```

**Frontend (Port 3000):**
```bash
lsof -ti:3000 | xargs kill -9
```

### No Captions Available

Some videos don't have captions. Error will show:
```
No captions found for this video
```

**Solution:** Try a different video with available captions.

### Python Version Issues

Some packages may have issues with Python 3.13. Use Python 3.11 or 3.12:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Slow Processing

If analysis takes longer than 60 seconds:
1. Check LM Studio is responsive
2. Check system resources (RAM, CPU)
3. Try a shorter video first

## 🚀 Deployment

For production deployment:

- Cloud deployments require cloud-based LM models instead of local LM Studio
- Consider AWS Lambda with API Gateway
- Use Google Cloud Run
- Try Azure Functions
- Or use OpenAI/Claude APIs instead of LM Studio

## 📈 Performance Tips

1. **Optimize LM Studio Model**
   - Use smaller models for faster processing
   - Larger models give better quality but slower results

2. **Batch Processing**
   - Process multiple videos in sequence
   - Avoid concurrent requests

3. **Caching**
   - Store results in database for repeated queries
   - Cache frequently accessed videos

## 🔐 Security Considerations

1. **No API Keys Stored** - All data processed locally
2. **No Video Downloads** - Only captions and metadata extracted
3. **CORS Enabled** - For frontend-backend communication
4. **Rate Limiting** - Recommended for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 Development

### Adding New Features

**Backend:**
- Add new endpoints in `backend/app/main.py`
- Add service logic in `backend/app/services/`
- Update models in `backend/app/models.py`

**Frontend:**
- Add new components in `frontend/components/`
- Update pages in `frontend/app/`
- Add API calls in `frontend/lib/api.ts`

### Testing

```bash
# Backend testing
cd backend
python -m pytest

# Frontend testing
cd frontend
npm test
```

## 📚 Documentation

Complete documentation is available in the `docs/` folder:

- **[API_GUIDE.md](docs/API_GUIDE.md)** - API endpoint documentation
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System architecture details
- **[FIXED_LOCALHOST_ISSUE.md](docs/FIXED_LOCALHOST_ISSUE.md)** - Connection troubleshooting
- **[INSTALLATION.md](docs/INSTALLATION.md)** - Installation instructions
- **[SETUP_AND_RUN.md](docs/SETUP_AND_RUN.md)** - Detailed setup guide
- **[COMMANDS.md](docs/COMMANDS.md)** - Command reference
- **[QUICKSTART.md](docs/QUICKSTART.md)** - Quick start guide
- **[SYSTEM_STATUS.md](docs/SYSTEM_STATUS.md)** - System status and verification

## 📄 License

This project is open source and available under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

For issues and questions:
1. Check the troubleshooting section above
2. See the documentation in the `docs/` folder
3. Check LM Studio logs for errors
4. Verify all dependencies are installed correctly
5. Ensure ports 3000 and 8000 are not in use

## 🗺️ Roadmap

- [ ] Multi-language subtitle support
- [ ] Speaker identification and analysis
- [ ] Keyword-based search within captions
- [ ] PDF report generation
- [ ] User authentication
- [ ] Video storage and history
- [ ] Batch video analysis
- [ ] Export to various formats (JSON, CSV, PDF)

---

**Made with ❤️ using FastAPI, Next.js, and LM Studio**
