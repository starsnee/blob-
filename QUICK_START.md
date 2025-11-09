# Quick Start Guide - Running Your App

## ✅ Prerequisites Checklist

Before running Expo, make sure these are running:

### 1. Backend Server (Required)
```bash
cd agent
./start.sh
```
**Check**: Visit http://localhost:8000/api/ping - should see `{"message":"pong"}`

### 2. ngrok (Required)
```bash
ngrok http 8000
```
**Check**: Look for the URL like `https://xxxxx.ngrok-free.dev`

### 3. Update config.ts
Make sure `config.ts` has the correct ngrok URL:
```typescript
export const API_BASE_URL = 'https://your-ngrok-url.ngrok-free.dev';
```

### 4. Start Expo
```bash
npm start
# or
npx expo start
```

## 🔍 Troubleshooting Connection Issues

### If the app shows "Backend Offline":

1. **Check if backend is running**:
   ```bash
   curl http://localhost:8000/api/ping
   ```
   Should return: `{"message":"pong"}`

2. **Check if ngrok is running**:
   ```bash
   curl http://localhost:4040/api/tunnels
   ```
   Should return JSON with tunnel information

3. **Test ngrok URL directly**:
   ```bash
   curl -H "ngrok-skip-browser-warning: true" https://your-ngrok-url.ngrok-free.dev/api/ping
   ```
   Should return: `{"message":"pong"}`

4. **Check Expo console**:
   - Look for "Fetching from:" log message
   - Check for any error messages
   - Look for network errors

### Common Issues:

#### Issue: "Network request failed"
- **Cause**: ngrok not running or wrong URL
- **Fix**: Start ngrok and update config.ts

#### Issue: "Expected JSON but got HTML"
- **Cause**: ngrok free tier showing browser warning page
- **Fix**: The app should handle this, but you can upgrade ngrok or use ngrok authtoken

#### Issue: "CORS error"
- **Cause**: Backend CORS not configured correctly
- **Fix**: Backend should already have CORS configured, but check agent/main.py

#### Issue: Backend not starting
- **Cause**: Virtual environment not activated or dependencies missing
- **Fix**: 
  ```bash
  cd agent
  source venv/bin/activate
  pip install -r requirements.txt  # if needed
  ./start.sh
  ```

## 📱 Running on Different Platforms

### iOS Simulator:
```bash
npm start
# Then press 'i' in the terminal
```

### Android Emulator:
```bash
npm start
# Then press 'a' in the terminal
```

### Physical Device:
```bash
npm start
# Scan QR code with Expo Go app
```

## 🚀 Quick Start Script

Run this to check everything:
```bash
./check_connection.sh
```

This will verify:
- ✅ Backend is running
- ✅ ngrok is running  
- ✅ ngrok URL is accessible
- ✅ config.ts has correct URL

## 📝 Important Notes

1. **ngrok URLs change**: Free ngrok URLs change each time you restart ngrok. Update `config.ts` when this happens.

2. **Two terminals needed**:
   - Terminal 1: Backend server (`./start.sh`)
   - Terminal 2: ngrok (`ngrok http 8000`)
   - Terminal 3: Expo (`npm start`)

3. **Mobile devices**: Make sure your phone and computer are on the same network for Expo Go, or use ngrok for remote access.

4. **Check logs**: Always check the Expo console and backend logs for error messages.

