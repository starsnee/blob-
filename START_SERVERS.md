# Quick Start Guide

## Current Status ✅

- **Backend Server**: Running on `http://localhost:8000`
- **ngrok**: Running and exposing backend at `https://enlightenedly-nonexcessive-le.ngrok-free.dev`
- **Frontend Config**: Already configured with ngrok URL

## Running the Servers

### Option 1: Already Running (Current)
The servers are already started in the background.

### Option 2: Manual Start

#### Start Backend (Python 3.12):
```bash
cd agent
./start.sh
```

Or manually:
```bash
cd agent
source venv/bin/activate
python -m uvicorn main:app --reload --port 8000 --host 0.0.0.0
```

#### Start ngrok (in another terminal):
```bash
ngrok http 8000
```

#### Update config.ts (if ngrok URL changes):
Update the URL in `config.ts` with your new ngrok URL.

## Running Expo App

### Start Expo:
```bash
npm start
# or
npx expo start
```

### Then:
1. Press `i` for iOS simulator
2. Press `a` for Android emulator  
3. Scan QR code with Expo Go app on your phone

## Testing the Connection

The app will automatically:
1. Connect to the backend via ngrok
2. Call `/api/ping` endpoint
3. Display connection status:
   - ✅ Green = Connected
   - ❌ Red = Disconnected
   - ⏳ Orange = Checking

## Stopping Servers

To stop the background processes:
```bash
# Find and kill backend
pkill -f "uvicorn main:app"

# Find and kill ngrok
pkill -f "ngrok http 8000"
```

## Troubleshooting

### Backend not responding?
```bash
curl http://localhost:8000/api/ping
```
Should return: `{"message":"pong"}`

### ngrok not working?
```bash
curl -H "ngrok-skip-browser-warning: true" https://enlightenedly-nonexcessive-le.ngrok-free.dev/api/ping
```
Should return: `{"message":"pong"}`

### Frontend can't connect?
1. Check that ngrok URL in `config.ts` matches your ngrok URL
2. Make sure backend is running on port 8000
3. Check Expo console for error messages

## Notes

- ngrok free tier URLs change each time you restart ngrok
- Update `config.ts` if the ngrok URL changes
- Backend logs are in `/tmp/backend.log`
- ngrok web interface: http://localhost:4040

