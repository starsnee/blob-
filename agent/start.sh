#!/bin/bash
# Start the backend server with Python 3.12
cd "$(dirname "$0")"
source venv/bin/activate
python -m uvicorn main:app --reload --port 8000 --host 0.0.0.0

