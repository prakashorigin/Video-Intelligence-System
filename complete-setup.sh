#!/bin/bash

# Video Intelligence System - Complete Setup & Run Guide
# This script will fix all issues and get everything running

set -e  # Exit on error

PROJECT_DIR="/Users/prakash/Python-program/video-intelligence-system"
cd "$PROJECT_DIR"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  Video Intelligence System - Complete Setup                    ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Function to print steps
print_step() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "→ $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# STEP 1: Setup Backend
print_step "STEP 1: Setting up Backend (Python)"

cd "$PROJECT_DIR/backend"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3.11 -m venv venv 2>/dev/null || python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "📥 Installing Python dependencies..."
pip install --quiet -r requirements.txt

# Create .env file
if [ ! -f ".env" ]; then
    echo "📝 Creating .env configuration..."
    cp .env.example .env
    echo "⚠️  Make sure LM Studio is running on port 1234"
fi

echo "✅ Backend setup complete"

# STEP 2: Setup Frontend
print_step "STEP 2: Setting up Frontend (Node.js)"

cd "$PROJECT_DIR/frontend"

# Install npm dependencies
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies (this may take 2-3 minutes)..."
    npm install --quiet
fi

# Create .env.local if not exists
if [ ! -f ".env.local" ]; then
    echo "📝 Creating frontend environment..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
fi

echo "✅ Frontend setup complete"

# STEP 3: Git Setup
print_step "STEP 3: Setting up Git Repository"

cd "$PROJECT_DIR"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Video Intelligence System"
    echo "✅ Git initialized"
else
    echo "✅ Git already initialized"
fi

print_step "STARTUP INSTRUCTIONS"

echo ""
echo "🎬 YOUR SYSTEM IS READY!"
echo ""
echo "Now follow these steps to run the application:"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "📌 STEP 1: Start LM Studio (Required)"
echo "   1. Open LM Studio application"
echo "   2. Search for: smollm-360m-instruct-v0.2"
echo "   3. Click Load Model"
echo "   4. Click 'Start Local Server'"
echo "   5. Wait for: 'Server is running on http://localhost:1234'"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "📌 STEP 2: Start Backend Server"
echo ""
echo "   Run this in Terminal 1:"
echo ""
echo "   cd $PROJECT_DIR"
echo "   source backend/venv/bin/activate"
echo "   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "   ✓ Wait for: 'Uvicorn running on http://0.0.0.0:8000'"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "📌 STEP 3: Start Frontend Server"
echo ""
echo "   Run this in Terminal 2:"
echo ""
echo "   cd $PROJECT_DIR/frontend"
echo "   npm run dev"
echo ""
echo "   ✓ Wait for: 'Ready in' message"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "📌 STEP 4: Open Your Browser"
echo ""
echo "   🌐 Visit: http://localhost:3000"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "🧪 VERIFY EVERYTHING IS WORKING:"
echo ""
echo "   Backend Health Check:"
echo "   curl http://localhost:8000/health"
echo ""
echo "   API Documentation:"
echo "   http://localhost:8000/docs"
echo ""
echo "   Frontend:"
echo "   http://localhost:3000"
echo ""
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "✅ Setup Complete!"
echo ""
