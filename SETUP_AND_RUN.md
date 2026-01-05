# 🚀 COMPLETE SETUP & RUN GUIDE

## Problem & Solution

**Error:** `localhost refused to connect` & `ERR_CONNECTION_REFUSED`

**Cause:** The backend and frontend services are not running

**Solution:** Follow this exact step-by-step guide

---

## ⚡ Quick Fix (5 minutes)

### 1️⃣ Run Complete Setup Script

```bash
cd /Users/prakash/Python-program/video-intelligence-system
bash complete-setup.sh
```

This will:
- ✅ Create Python virtual environment
- ✅ Install backend dependencies
- ✅ Install frontend dependencies
- ✅ Setup all configuration files
- ✅ Initialize Git repository

---

## 🎯 Detailed Startup Instructions

### Prerequisites Check

```bash
python3 --version     # Should show 3.11+
node --version        # Should show 18+
npm --version         # Should show 8+
```

### Terminal 1: Start Backend Server

```bash
cd /Users/prakash/Python-program/video-intelligence-system
source backend/venv/bin/activate
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**✅ When you see this, Backend is READY**

---

### Terminal 2: Start Frontend Server

```bash
cd /Users/prakash/Python-program/video-intelligence-system/frontend
npm run dev
```

**Expected Output:**
```
- Local:        http://localhost:3000
- Ready in XXXms
```

**✅ When you see this, Frontend is READY**

---

### Terminal 3: Start LM Studio (Required!)

**Important:** LM Studio must be running for AI analysis to work

1. **Open LM Studio Application** (download from https://lmstudio.ai)
2. **Search for Model:** `smollm-360m-instruct-v0.2`
3. **Download the Model** (if not already downloaded)
4. **Load the Model:** Click on the downloaded model
5. **Start Local Server:** Click "Start Local Server" button
6. **Verify:** You should see `Server is running on http://localhost:1234`

---

## 🌐 Access Your Application

Once all three services are running, open your browser:

| Service | URL | Purpose |
|---------|-----|---------|
| **Application** | http://localhost:3000 | Main web interface |
| **API** | http://localhost:8000 | Backend API |
| **API Docs** | http://localhost:8000/docs | Interactive documentation |
| **LM Studio** | http://localhost:1234 | AI model interface |

---

## ✅ Verification Checklist

### Backend Running?

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

### Frontend Running?

Open: **http://localhost:3000**

Should see the Video Intelligence System interface with input form.

### LM Studio Running?

Open: **http://localhost:1234**

Should see the LM Studio interface.

---

## 📝 First Test: Analyze a Video

1. Open **http://localhost:3000** in your browser
2. You should see the **Video Intelligence System** interface
3. Paste a YouTube URL (example below)
4. Click **"Analyze Video"**
5. Wait 20-40 seconds
6. View results

**Example YouTube URL:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

## 🐛 Troubleshooting Connection Issues

### Error: "ERR_CONNECTION_REFUSED" on localhost:3000

**Problem:** Frontend is not running

**Solution:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system/frontend
npm run dev
```

Wait for "Ready in XXXms" message.

---

### Error: "ERR_CONNECTION_REFUSED" on localhost:8000

**Problem:** Backend is not running

**Solution:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system
source backend/venv/bin/activate
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Wait for "Uvicorn running on http://0.0.0.0:8000" message.

---

### Error: "LM Studio service is not available"

**Problem:** LM Studio not running or not accessible

**Solution:**
1. Open LM Studio application
2. Load the model: `smollm-360m-instruct-v0.2`
3. Click "Start Local Server"
4. Verify http://localhost:1234 is accessible

---

### Error: "Port 8000 already in use"

**Solution:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Then run backend again
```

---

### Error: "Port 3000 already in use"

**Solution:**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Then run frontend again
```

---

## 🔄 Complete Fresh Start

If something is broken, do a complete fresh start:

```bash
# Kill all services
lsof -ti:3000 | xargs kill -9 2>/dev/null
lsof -ti:8000 | xargs kill -9 2>/dev/null

# Run setup script
cd /Users/prakash/Python-program/video-intelligence-system
bash complete-setup.sh

# Follow startup instructions above
```

---

## 🌐 GitHub Setup

### Initialize Git (One Time Only)

```bash
cd /Users/prakash/Python-program/video-intelligence-system

# Already initialized by setup script, but you can do it manually:
git init
git add .
git commit -m "Initial commit: Video Intelligence System"
```

### Push to GitHub

```bash
# Add remote (replace with your repository URL)
git remote add origin https://github.com/prakashorigin/Video-Intelligence-System.git

# Set main as default branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Future Commits

```bash
# After making changes
git add .
git commit -m "Your commit message"
git push origin main
```

---

## 📊 Service Status Summary

| Service | Port | Status Check | Startup Command |
|---------|------|--------------|-----------------|
| **Backend** | 8000 | curl http://localhost:8000/health | `python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` |
| **Frontend** | 3000 | http://localhost:3000 | `npm run dev` |
| **LM Studio** | 1234 | http://localhost:1234 | Use LM Studio app |

---

## 🆘 Still Having Issues?

### Backend won't start?

```bash
# Check Python version
python3 --version

# Verify dependencies
pip list | grep fastapi

# Try installing again
pip install -r requirements.txt
```

### Frontend won't start?

```bash
# Verify Node.js
node --version
npm --version

# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Can't connect to localhost?

```bash
# Check if ports are in use
lsof -i :3000
lsof -i :8000
lsof -i :1234

# Try with different ports
# Backend: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
# Frontend: PORT=3001 npm run dev
```

---

## 🎯 Success Indicators

✅ Backend Running:
- Terminal shows: "Uvicorn running on http://0.0.0.0:8000"
- Health check returns: `{"status": "healthy", ...}`

✅ Frontend Running:
- Terminal shows: "Ready in XXXms"
- Browser shows: Video Intelligence System interface

✅ LM Studio Running:
- Application window shows model is loaded
- Server running message displays

✅ Everything Connected:
- Can analyze videos
- Results display properly

---

## 📞 Quick Reference

**Start Backend:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system/backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Start Frontend:**
```bash
cd /Users/prakash/Python-program/video-intelligence-system/frontend
npm run dev
```

**Start LM Studio:**
- Open LM Studio app → Load model → Click "Start Local Server"

**Access Application:**
- http://localhost:3000

**Test API:**
- http://localhost:8000/docs (Swagger UI)

---

## ✨ You're Ready!

After following these steps:

✅ Backend running on http://localhost:8000
✅ Frontend running on http://localhost:3000
✅ AI engine running on http://localhost:1234
✅ Ready to analyze videos!

**Next Step:** Visit http://localhost:3000 and analyze your first video!

---

*For complete documentation, see [README.md](README.md)*
