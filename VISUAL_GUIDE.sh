#!/usr/bin/env bash

# =============================================================================
# VISUAL SETUP GUIDE FOR VIDEO INTELLIGENCE SYSTEM
# =============================================================================
# Run this to see step-by-step what to do

cat << 'EOF'

╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║       VIDEO INTELLIGENCE SYSTEM - COMPLETE SETUP GUIDE                   ║
║                                                                           ║
║          Everything you need to get the system running                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════════

STEP 1: ONE-TIME SETUP
─────────────────────────────────────────────────────────────────────────

Open Terminal and run:

    bash /Users/prakash/Python-program/video-intelligence-system/setup.sh

This will:
  ✓ Create Python virtual environment
  ✓ Install Python dependencies
  ✓ Install Node.js dependencies
  ✓ Create configuration files
  ✓ Initialize Git repository

Wait for: "✅ Setup Complete!"

═══════════════════════════════════════════════════════════════════════════

STEP 2: START BACKEND SERVER
─────────────────────────────────────────────────────────────────────────

Open TERMINAL 1 and run:

    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh

Expected output:
  ✅ Backend is starting...
  🌐 Access at: http://localhost:8000
  📖 API Docs: http://localhost:8000/docs
  INFO: Uvicorn running on http://0.0.0.0:8000
  INFO: Application startup complete

When you see: "Uvicorn running on http://0.0.0.0:8000"
→ Backend is READY (keep this terminal open)

═══════════════════════════════════════════════════════════════════════════

STEP 3: START FRONTEND SERVER
─────────────────────────────────────────────────────────────────────────

Open TERMINAL 2 and run:

    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh

Expected output:
  ✅ Frontend is starting...
  🌐 Access at: http://localhost:3000
  Ready in XXXms

When you see: "Ready in XXXms"
→ Frontend is READY (keep this terminal open)

═══════════════════════════════════════════════════════════════════════════

STEP 4: START LM STUDIO (IMPORTANT!)
─────────────────────────────────────────────────────────────────────────

Without this step, AI analysis won't work!

1. Open the LM Studio application
   (Download from https://lmstudio.ai if you don't have it)

2. In the search box, type:
   smollm-360m-instruct-v0.2

3. Click the model to DOWNLOAD it (if not already downloaded)

4. Click on the downloaded model to LOAD it

5. Look for "Start Local Server" button and CLICK IT

6. Wait for message:
   "Server is running on http://localhost:1234"

When you see this message:
→ LM Studio is READY

═══════════════════════════════════════════════════════════════════════════

STEP 5: OPEN APPLICATION IN BROWSER
─────────────────────────────────────────────────────────────────────────

Open your web browser and visit:

    http://localhost:3000

You should see:
  ✓ Video Intelligence System title
  ✓ URL input field
  ✓ "Analyze Video" button

If you see this → Everything is working!

═══════════════════════════════════════════════════════════════════════════

STEP 6: TEST WITH A VIDEO
─────────────────────────────────────────────────────────────────────────

1. Copy this YouTube URL:
   https://www.youtube.com/watch?v=dQw4w9WgXcQ

2. Paste it into the input field

3. Click "Analyze Video"

4. Wait 20-40 seconds

5. View the results!

═══════════════════════════════════════════════════════════════════════════

✅ SERVICE LOCATIONS
─────────────────────────────────────────────────────────────────────────

Frontend Application:    http://localhost:3000
Backend API:             http://localhost:8000
API Documentation:       http://localhost:8000/docs
LM Studio Interface:     http://localhost:1234

═══════════════════════════════════════════════════════════════════════════

🧪 VERIFY EVERYTHING IS WORKING
─────────────────────────────────────────────────────────────────────────

Option 1: Check backend health

    curl http://localhost:8000/health

Expected response should include:
    "status": "healthy"

Option 2: Check frontend

    Visit http://localhost:3000 in browser

Should show Video Intelligence System interface

Option 3: Check API docs

    Visit http://localhost:8000/docs in browser

Should show Swagger UI with endpoints

═══════════════════════════════════════════════════════════════════════════

🆘 TROUBLESHOOTING
─────────────────────────────────────────────────────────────────────────

PROBLEM: "localhost refused to connect"

SOLUTION:
  - Make sure backend is running (Terminal 1)
  - Make sure frontend is running (Terminal 2)
  - Check the terminal output for errors
  - Refresh the browser page

PROBLEM: "ERR_CONNECTION_REFUSED"

SOLUTION:
  - Backend not running? Run in Terminal 1:
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh

  - Frontend not running? Run in Terminal 2:
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh

PROBLEM: "Port 8000 already in use"

SOLUTION:
  - Kill process using port 8000:
    lsof -ti:8000 | xargs kill -9
  - Then restart backend

PROBLEM: "LM Studio service is not available"

SOLUTION:
  - Open LM Studio application
  - Load model: smollm-360m-instruct-v0.2
  - Click "Start Local Server"
  - Wait for "Server is running on http://localhost:1234"

PROBLEM: No captions found error

SOLUTION:
  - Try a different YouTube video
  - Some videos don't have captions available
  - Educational videos usually have captions

═══════════════════════════════════════════════════════════════════════════

📝 QUICK COMMANDS REFERENCE
─────────────────────────────────────────────────────────────────────────

Setup (one time):
    bash /Users/prakash/Python-program/video-intelligence-system/setup.sh

Start backend (Terminal 1):
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh

Start frontend (Terminal 2):
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh

Open application:
    http://localhost:3000

═══════════════════════════════════════════════════════════════════════════

🔄 IF SOMETHING GOES WRONG
─────────────────────────────────────────────────────────────────────────

Kill all services and start fresh:

    # Kill processes
    lsof -ti:3000 | xargs kill -9 2>/dev/null
    lsof -ti:8000 | xargs kill -9 2>/dev/null

    # Run setup again
    bash /Users/prakash/Python-program/video-intelligence-system/setup.sh

    # Start services in new terminals
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-backend.sh
    bash /Users/prakash/Python-program/video-intelligence-system/quick-start-frontend.sh

═══════════════════════════════════════════════════════════════════════════

🌐 GITHUB SETUP (OPTIONAL)
─────────────────────────────────────────────────────────────────────────

First time push to GitHub:

    cd /Users/prakash/Python-program/video-intelligence-system
    git remote add origin https://github.com/prakashorigin/Video-Intelligence-System.git
    git branch -M main
    git push -u origin main

Future pushes:

    cd /Users/prakash/Python-program/video-intelligence-system
    git add .
    git commit -m "Your message"
    git push origin main

═══════════════════════════════════════════════════════════════════════════

✨ SUCCESS INDICATORS
─────────────────────────────────────────────────────────────────────────

✅ Backend Running:
   - Terminal 1 shows "Uvicorn running on http://0.0.0.0:8000"
   - curl http://localhost:8000/health works

✅ Frontend Running:
   - Terminal 2 shows "Ready in XXXms"
   - http://localhost:3000 loads in browser

✅ LM Studio Running:
   - LM Studio window shows server running message
   - http://localhost:1234 is accessible

✅ Everything Connected:
   - Can analyze videos
   - Results display properly
   - No error messages

═══════════════════════════════════════════════════════════════════════════

🎉 YOU'RE READY!
─────────────────────────────────────────────────────────────────────────

Your Video Intelligence System is ready to use!

Remember:
  1. Run setup.sh (one time only)
  2. Start backend in Terminal 1
  3. Start frontend in Terminal 2
  4. Start LM Studio app
  5. Visit http://localhost:3000

Happy analyzing! 🎬🤖

═══════════════════════════════════════════════════════════════════════════

Questions? See the documentation:
  - SETUP_AND_RUN.md
  - COMMANDS.md
  - README.md

═══════════════════════════════════════════════════════════════════════════

EOF
