#!/bin/bash
# Start the backend server with Python 3.12
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
if ! python -c "import fastapi, uvicorn, pydantic" 2>/dev/null; then
    echo "⚠️  Missing dependencies. Installing..."
    pip install -r requirements.txt
fi

echo "✅ Starting backend server on port 8000..."
python -m uvicorn main:app --reload --port 8000 --host 0.0.0.0

