#!/bin/bash

# Video Intelligence System - Frontend Startup Script

echo "🚀 Starting Video Intelligence System Frontend..."

# Navigate to frontend directory
cd "$(dirname "$0")/frontend" || exit 1

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "📝 Creating .env.local file..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
fi

# Start the frontend development server
echo "🎯 Starting Next.js development server on http://localhost:3000"
echo ""

npm run dev
