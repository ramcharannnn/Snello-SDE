#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start FastAPI backend in background
uvicorn main:app --reload &
SERVER_PID=$!

# Wait a moment for server to spin up
sleep 2

# Open web UI
xdg-open web/index.html

# Wait until user presses enter to kill server
echo "Press [ENTER] to stop chatbot..."
read

# Kill FastAPI server
kill $SERVER_PID
