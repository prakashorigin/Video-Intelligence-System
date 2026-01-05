# 🚀 COPY-PASTE COMMANDS TO RUN YOUR SYSTEM

## ⚡ Super Quick Start (3 Commands)

### Command 1: Setup Everything (Run Once)
```bash
bash /Users/prakash/Python-program/video-intelligence-system/setup.sh
```

### Command 2: Start Backend (Terminal 1)
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh
```

**Wait for message:** `Uvicorn running on http://0.0.0.0:8000`

### Command 3: Start Frontend (Terminal 2)
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh
```

**Wait for message:** `Ready in XXXms`

### Open Browser
```
http://localhost:3000
```

---

## 📋 Step-by-Step Commands

### Step 1: Initial Setup (One Time)

```bash
cd /Users/prakash/Python-program/video-intelligence-system
bash setup.sh
```

---

### Step 2: Terminal 1 - Start Backend

```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh
```

**Expected Output:**
```
✅ Backend is starting...

🌐 Access at: http://localhost:8000
📖 API Docs: http://localhost:8000/docs

INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

✅ **Backend is READY when you see this**

---

### Step 3: Terminal 2 - Start Frontend

```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh
```

**Expected Output:**
```
✅ Frontend is starting...

🌐 Access at: http://localhost:3000

Ready in XXXms
```

✅ **Frontend is READY when you see this**

---

### Step 4: Start LM Studio (Required!)

1. Open **LM Studio** application
2. Search for: `smollm-360m-instruct-v0.2`
3. Click the model to load it
4. Click **"Start Local Server"** button
5. Wait for message: `Server is running on http://localhost:1234`

✅ **LM Studio is READY when you see this**

---

### Step 5: Open in Browser

Open your browser and visit:

```
http://localhost:3000
```

You should see the **Video Intelligence System** interface.

---

## 🧪 Quick Verification

### Check Backend Health

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

### Check Frontend

Visit: `http://localhost:3000`

Should show the input form.

### Check API Documentation

Visit: `http://localhost:8000/docs`

Should show Swagger UI with all endpoints.

---

## 🎬 First Test

1. Visit **http://localhost:3000**
2. Enter YouTube URL:
   ```
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```
3. Click **"Analyze Video"**
4. Wait 20-40 seconds
5. View the results!

---

## 🆘 Troubleshooting Commands

### If ports are in use

```bash
# Kill backend on port 8000
lsof -ti:8000 | xargs kill -9

# Kill frontend on port 3000
lsof -ti:3000 | xargs kill -9

# Then restart services
```

### If backend dependencies fail

```bash
cd /Users/prakash/Python-program/video-intelligence-system/backend
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### If frontend dependencies fail

```bash
cd /Users/prakash/Python-program/video-intelligence-system/frontend
rm -rf node_modules package-lock.json
npm install
```

### Fresh restart

```bash
# Kill all services
lsof -ti:3000 | xargs kill -9 2>/dev/null
lsof -ti:8000 | xargs kill -9 2>/dev/null

# Restart
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh &
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh &
```

---

## 🔗 GitHub Setup Commands

### Initialize Git (One Time)

```bash
cd /Users/prakash/Python-program/video-intelligence-system

# Already done by setup.sh, but you can do it again:
git init
git add .
git commit -m "Initial commit: Video Intelligence System"
```

### Add Remote Repository

```bash
cd /Users/prakash/Python-program/video-intelligence-system

git remote add origin https://github.com/prakashorigin/Video-Intelligence-System.git
git branch -M main
git push -u origin main
```

### Push Future Changes

```bash
cd /Users/prakash/Python-program/video-intelligence-system

git add .
git commit -m "Your commit message"
git push origin main
```

---

## 📊 Service URLs

Once everything is running:

| Service | URL |
|---------|-----|
| Application | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |
| LM Studio | http://localhost:1234 |

---

## ✅ Success Checklist

- [ ] Run setup.sh
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] LM Studio running on port 1234
- [ ] Can access http://localhost:3000
- [ ] Can access http://localhost:8000/docs
- [ ] Analyzed first video successfully

---

## 🎯 Quick Reference

**One-time setup:**
```bash
bash /Users/prakash/Python-program/video-intelligence-system/setup.sh
```

**Start backend (Terminal 1):**
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh
```

**Start frontend (Terminal 2):**
```bash
bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh
```

**Visit app:**
```
http://localhost:3000
```

---

## 🎉 That's It!

Your Video Intelligence System is ready to use!

**Remember:**
1. ✅ Run setup.sh (one time)
2. ✅ Start backend
3. ✅ Start frontend
4. ✅ Start LM Studio
5. ✅ Visit http://localhost:3000

Enjoy analyzing videos! 🎬🤖
