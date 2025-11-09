#!/bin/bash
# Start the Google/Notion API server with Python 3.12
cd "$(dirname "$0")"
source venv/bin/activate
python -m uvicorn GN_main:app --reload --port 8001 --host 0.0.0.0

