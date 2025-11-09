#!/bin/bash
# Start the Google/Notion API server with Python 3.12
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3.12 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Check if dependencies are installed
if ! python -c "import fastapi, uvicorn, notion_client, google_auth_oauthlib" 2>/dev/null; then
    echo "⚠️  Missing dependencies. Installing..."
    pip install -r requirements.txt
fi

echo "✅ Starting Google/Notion API server on port 8001..."
python -m uvicorn GN_main:app --reload --port 8001 --host 0.0.0.0

