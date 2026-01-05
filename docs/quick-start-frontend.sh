#!/bin/bash

# Quick Frontend Startup Script
# Run this in Terminal 2

PROJECT_DIR="/Users/prakash/Python-program/video-intelligence-system"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        Starting Video Intelligence System Frontend             ║"
echo "║                     PORT: 3000                                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

cd "$PROJECT_DIR/frontend"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies (this may take a few minutes)..."
    npm install
fi

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
    echo "📝 Created .env.local file"
fi

echo ""
echo "✅ Frontend is starting..."
echo ""
echo "🌐 Access at: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the frontend development server
npm run dev
