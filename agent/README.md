# Blob Backend

FastAPI backend server for the Blob app.

## Setup

1. Install dependencies:
```bash
pip3 install fastapi 'uvicorn[standard]' pydantic requests
```

## Running the Server

### Quick Start (Recommended):
```bash
cd agent
./start.sh
```

### Manual Start:
```bash
cd agent
source venv/bin/activate
python -m uvicorn main:app --reload --port 8000
```

**Note**: This project uses Python 3.12 in a virtual environment. The `start.sh` script automatically activates the venv.

The server will be available at `http://localhost:8000`

## Endpoints

- `GET /api/ping` - Health check endpoint (returns `{"message": "pong"}`)
- `GET /health` - Health check endpoint (returns `{"status": "ok"}`)
- `POST /api/chat` - Chat endpoint using NVIDIA Nemotron (requires `NVIDIA_API_KEY` environment variable)

## Environment Variables

- `NVIDIA_API_KEY` - Required for the `/api/chat` endpoint

## Testing

Test the ping endpoint:
```bash
curl http://localhost:8000/api/ping
```

## ngrok Setup

To expose the server for mobile testing:

1. Install ngrok: https://ngrok.com/download
2. Start ngrok:
```bash
ngrok http 8000
```
3. Update the `API_BASE_URL` in `../config.ts` with your ngrok URL

