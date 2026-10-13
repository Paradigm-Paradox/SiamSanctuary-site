#!/usr/bin/env bash
# Start the local development webserver with hot-reloading
cd "$(dirname "$0")"
echo "Starting DreamNails.Asia Development Server..."
echo "Preview will be available at: http://localhost:4321/"
echo "Press Ctrl+C to stop."
npm run dev
