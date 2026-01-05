#!/bin/bash

# Complete Setup Script
# Run once to setup everything

PROJECT_DIR="/Users/prakash/Python-program/video-intelligence-system"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║      Video Intelligence System - Complete Setup               ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Backend Setup
echo "🔧 Setting up Backend..."
cd "$PROJECT_DIR/backend"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

source venv/bin/activate
pip install -q -r requirements.txt
echo "✅ Backend dependencies installed"

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Backend .env created"
fi

# Frontend Setup
echo ""
echo "🔧 Setting up Frontend..."
cd "$PROJECT_DIR/frontend"

if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies (this may take a moment)..."
    npm install --quiet
    echo "✅ Frontend dependencies installed"
fi

if [ ! -f ".env.local" ]; then
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
    echo "✅ Frontend .env.local created"
fi

# Git Setup
echo ""
echo "🔧 Setting up Git..."
cd "$PROJECT_DIR"

if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "Initial commit: Video Intelligence System" > /dev/null 2>&1
    echo "✅ Git repository initialized"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              ✅ Setup Complete!                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Now run these commands in separate terminals:"
echo ""
echo "Terminal 1 - Backend Server:"
echo "  bash $PROJECT_DIR/quick-start-backend.sh"
echo ""
echo "Terminal 2 - Frontend Server:"
echo "  bash $PROJECT_DIR/quick-start-frontend.sh"
echo ""
echo "Terminal 3 - Start LM Studio:"
echo "  1. Open LM Studio app"
echo "  2. Load: smollm-360m-instruct-v0.2"
echo "  3. Click: Start Local Server"
echo ""
echo "Then visit: http://localhost:3000"
echo ""
