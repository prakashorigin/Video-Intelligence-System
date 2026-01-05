# Installation & Setup Guide

## System Requirements

- **Python:** 3.11 or 3.12 (NOT 3.13)
- **Node.js:** 18+ with npm
- **LM Studio:** Latest version installed and running
- **RAM:** 4GB minimum (8GB recommended)
- **Disk Space:** 5GB for LM Studio model

---

## Step 1: Clone/Download Project

```bash
cd /Users/prakash/Python-program/video-intelligence-system
```

---

## Step 2: Setup Backend

### 2.1 Create Virtual Environment

```bash
cd backend
python3.11 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 2.2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.3 Setup Environment Variables

```bash
cp .env.example .env
```

Edit `.env` file and set your LM Studio configuration:

```env
LM_STUDIO_URL=http://localhost:1234
LM_STUDIO_MODEL=smollm-360m-instruct-v0.2
```

---

## Step 3: Setup Frontend

### 3.1 Install Dependencies

```bash
cd frontend
npm install
```

### 3.2 Create Environment File

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Step 4: Setup LM Studio

### 4.1 Install LM Studio

- Download from [lmstudio.ai](https://lmstudio.ai)
- Install on your system

### 4.2 Download Model

1. Open LM Studio
2. Click on "Search models"
3. Search: `smollm-360m-instruct-v0.2`
4. Click download
5. Wait for model to download (~500MB)

### 4.3 Start Local Server

1. Load the model: Click on the downloaded model
2. Click "Start Local Server"
3. Wait for server to be ready
4. Verify at: `http://localhost:1234`

---

## Step 5: Run Application

### Option A: Separate Terminals (Recommended)

**Terminal 1 - Backend:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system
./start-backend.sh
```

Wait for: `Uvicorn running on http://0.0.0.0:8000`

**Terminal 2 - Frontend:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system
./start-frontend.sh
```

Wait for: `Ready in [X] ms`

Then open: **http://localhost:3000**

---

### Option B: Single Terminal with tmux

```bash
cd /Users/prakash/Python-program/video-intelligence-system
./start-tmux.sh
```

This will:
1. Create tmux session with 2 windows
2. Start backend in window 0
3. Start frontend in window 1
4. Automatically attach to the session

Exit tmux: Press `Ctrl+B` then type `:kill-session`

---

### Option C: Manual Commands

**Backend (Terminal 1):**
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend (Terminal 2):**
```bash
cd frontend
npm run dev
```

---

## Step 6: Verify Installation

### Backend Health Check

```bash
curl http://localhost:8000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "lm_studio_available": true
}
```

### Frontend Access

Open: **http://localhost:3000**

Should see the Video Intelligence System interface.

### API Documentation

Visit: **http://localhost:8000/docs**

Should see Swagger UI with all available endpoints.

---

## Verification Checklist

- [ ] Python 3.11+ installed
- [ ] Node.js 18+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (both backend and frontend)
- [ ] .env files created with correct URLs
- [ ] LM Studio installed
- [ ] Model downloaded in LM Studio
- [ ] LM Studio local server running
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Can access http://localhost:3000
- [ ] Health check returns lm_studio_available: true

---

## Troubleshooting

### Backend fails to start

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
cd backend
source venv/bin/activate  # Ensure venv is active
pip install -r requirements.txt
```

**Error:** `Port 8000 already in use`

**Solution:**
```bash
lsof -ti:8000 | xargs kill -9
```

---

### Frontend fails to start

**Error:** `npm: command not found`

**Solution:** Install Node.js from [nodejs.org](https://nodejs.org)

**Error:** `Port 3000 already in use`

**Solution:**
```bash
lsof -ti:3000 | xargs kill -9
```

---

### LM Studio Connection Failed

**Error:** `LM Studio service is not available`

**Checklist:**
1. Is LM Studio open? ✓
2. Is model loaded? ✓
3. Is local server started? ✓
4. Is LM_STUDIO_URL correct in .env? ✓
5. Can you access http://localhost:1234 in browser? ✓

**Solution:** Restart LM Studio and try again

---

### No Captions Error

**Error:** `No captions found for this video`

**Causes:**
- Video has no captions available
- Video is age-restricted
- Video from private channel

**Solution:** Try a different video with captions

---

### Slow Analysis

**Performance Issues:**
- LM Studio using smaller model takes 20-40 seconds
- This is normal
- Processing faster than 20s is not guaranteed

**To optimize:**
1. Check LM Studio CPU/Memory usage
2. Close unnecessary applications
3. Use smaller model size (if available)

---

## First Test Analysis

1. Navigate to http://localhost:3000
2. Paste this YouTube URL:
   ```
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```
3. Click "Analyze Video"
4. Wait 20-40 seconds
5. View results

---

## Next Steps

- Read the [README.md](README.md) for complete documentation
- Check [API_GUIDE.md](API_GUIDE.md) for API details
- Explore the Swagger UI at http://localhost:8000/docs
- Customize the frontend and backend as needed

---

**Installation Complete!** 🎉

The system is now ready to analyze YouTube videos.
