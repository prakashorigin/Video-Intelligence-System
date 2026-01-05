#!/bin/bash

# Video Intelligence System - Combined Startup Script (using tmux)

# Check if tmux is installed
if ! command -v tmux &> /dev/null; then
    echo "❌ tmux is not installed. Please install it first:"
    echo "   macOS: brew install tmux"
    echo "   Ubuntu/Debian: sudo apt-get install tmux"
    exit 1
fi

SESSION_NAME="video-intelligence"

# Create tmux session
echo "🚀 Creating tmux session: $SESSION_NAME"
tmux new-session -d -s $SESSION_NAME

# Start backend in first window
echo "🎯 Starting Backend..."
tmux send-keys -t $SESSION_NAME:0 "cd '$(dirname "$0")' && bash start-backend.sh" Enter

# Create new window for frontend
tmux new-window -t $SESSION_NAME -n frontend
echo "🎯 Starting Frontend..."
tmux send-keys -t $SESSION_NAME:1 "cd '$(dirname "$0")' && bash start-frontend.sh" Enter

# Display instructions
echo ""
echo "✅ Both services are starting in tmux session: $SESSION_NAME"
echo ""
echo "📖 View logs:"
echo "   - Backend:  tmux attach -t $SESSION_NAME:0"
echo "   - Frontend: tmux attach -t $SESSION_NAME:1"
echo ""
echo "🌐 Access the application:"
echo "   - Frontend:  http://localhost:3000"
echo "   - Backend API: http://localhost:8000"
echo "   - API Docs:  http://localhost:8000/docs"
echo ""
echo "⚠️  Kill session: tmux kill-session -t $SESSION_NAME"
echo ""

# Attach to session
tmux attach -t $SESSION_NAME
