#!/bin/bash

# Quick Backend Startup Script
# Run this in Terminal 1

PROJECT_DIR="/Users/prakash/Python-program/video-intelligence-system"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         Starting Video Intelligence System Backend             ║"
echo "║                     PORT: 8000                                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

cd "$PROJECT_DIR/backend"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Ensure dependencies are installed
echo "📥 Ensuring dependencies are installed..."
pip install -q -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "📝 Created .env file"
fi

echo ""
echo "✅ Backend is starting..."
echo ""
echo "🌐 Access at: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the backend server
cd "$PROJECT_DIR/backend"
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
