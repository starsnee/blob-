# Complete Setup Guide - Blob Project

This guide will help you set up the entire project (frontend + backend) on any machine.

## 📋 System Requirements

- **Node.js**: v18+ (comes with npm)
- **Python**: 3.10+ (3.12 recommended)
- **Git**: For version control
- **ngrok**: For exposing backend to mobile devices
- **Homebrew** (macOS) or package manager for your OS

---

## 🔧 Step 1: Install System Dependencies

### macOS (using Homebrew):
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js (if not installed)
brew install node

# Install Python 3.12
brew install python@3.12

# Install ngrok
brew install ngrok/ngrok/ngrok

# Verify installations
node --version    # Should be v18+
python3.12 --version  # Should be 3.12.x
ngrok version     # Should show version
```

### Linux (Ubuntu/Debian):
```bash
# Update package list
sudo apt update

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Python 3.12
sudo apt install -y python3.12 python3.12-venv python3-pip

# Install ngrok
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok

# Verify installations
node --version
python3.12 --version
ngrok version
```

### Windows:
1. Install Node.js from https://nodejs.org/
2. Install Python 3.12 from https://www.python.org/downloads/
3. Install ngrok from https://ngrok.com/download
4. Use Git Bash or WSL for terminal commands

---

## 📦 Step 2: Frontend Dependencies (React Native/Expo)

### All Required npm Packages:

```bash
cd /path/to/blob

# Install all frontend dependencies
npm install
```

**Complete list of npm packages installed:**

#### Production Dependencies:
- `@react-navigation/native@^7.1.19` - Navigation library
- `@react-navigation/native-stack@^7.6.2` - Stack navigator
- `expo@~54.0.23` - Expo framework
- `expo-status-bar@~3.0.8` - Status bar component
- `nativewind@^4.2.1` - Tailwind CSS for React Native
- `prettier-plugin-tailwindcss@^0.5.14` - Tailwind formatting
- `react@^19.1.0` - React library
- `react-native@0.81.5` - React Native framework
- `react-native-reanimated@^4.1.3` - Animation library
- `react-native-safe-area-context@^5.4.0` - Safe area handling
- `react-native-screens@^4.18.0` - Native screens
- `react-native-worklets@^0.6.1` - Worklets support
- `react-native-worklets-core@^1.6.2` - Worklets core
- `tailwindcss@^3.4.18` - Tailwind CSS

#### Development Dependencies:
- `@types/react@~19.1.0` - TypeScript types for React
- `babel-preset-expo@^54.0.7` - Babel preset for Expo
- `typescript@~5.9.2` - TypeScript compiler

**Installation command:**
```bash
npm install
```

---

## 🐍 Step 3: Backend Dependencies (Python)

### Main Backend (`agent/`)

**Required Python Packages:**
- `fastapi>=0.104.0` - Web framework
- `uvicorn[standard]>=0.24.0` - ASGI server
- `pydantic>=2.0.0` - Data validation
- `requests>=2.31.0` - HTTP library
- `python-dotenv>=1.0.0` - Environment variables

**Setup:**
```bash
cd agent

# Create virtual environment with Python 3.12
python3.12 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install fastapi 'uvicorn[standard]' pydantic requests python-dotenv
```

### Google/Notion API Backend (`google-notion_api/`)

**Required Python Packages:**
- `fastapi>=0.104.0` - Web framework
- `uvicorn[standard]>=0.24.0` - ASGI server
- `pydantic>=2.0.0` - Data validation
- `python-dotenv>=1.0.0` - Environment variables
- `httpx>=0.24.0` - Async HTTP client
- `notion-client>=2.2.0` - Notion API client
- `google-auth-oauthlib>=1.0.0` - Google OAuth
- `google-auth>=2.23.0` - Google authentication
- `google-api-python-client>=2.100.0` - Google API client

**Setup:**
```bash
cd google-notion_api

# Create virtual environment with Python 3.12
python3.12 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Step 4: Complete Setup Process

### 1. Clone/Download the Project
```bash
git clone <your-repo-url> blob
cd blob
```

### 2. Install Frontend Dependencies
```bash
npm install
```

### 3. Set Up Main Backend
```bash
cd agent
python3.12 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install fastapi 'uvicorn[standard]' pydantic requests python-dotenv
cd ..
```

### 4. Set Up Google/Notion API Backend
```bash
cd google-notion_api
python3.12 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
cd ..
```

### 5. Configure ngrok
```bash
# Sign up at https://dashboard.ngrok.com/signup
# Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

### 6. Configure Environment Variables

**Main Backend (`agent/`):**
Create `agent/.env` (optional, for NVIDIA API):
```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

**Google/Notion API (`google-notion_api/`):**
Create `google-notion_api/.env`:
```env
# Notion OAuth
NOTION_CLIENT_ID=your_notion_client_id
NOTION_CLIENT_SECRET=your_notion_client_secret
NOTION_REDIRECT_URI=http://localhost:8001/auth/notion/callback
NOTION_ROOT_PAGE_ID=your_notion_root_page_id

# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8001/auth/google/callback
GOOGLE_CALENDAR_ID=primary
```

**Frontend (`config.ts`):**
Update with your ngrok URL after starting ngrok:
```typescript
export const API_BASE_URL = 'https://your-ngrok-url.ngrok-free.dev';
```

---

## ✅ Step 5: Verification

### Verify Frontend:
```bash
# Check Node.js version
node --version  # Should be v18+

# Check npm packages installed
npm list --depth=0

# Verify TypeScript
npx tsc --version
```

### Verify Main Backend:
```bash
cd agent
source venv/bin/activate
python --version  # Should be 3.12.x
pip list | grep -E "fastapi|uvicorn|pydantic"
```

### Verify Google/Notion API Backend:
```bash
cd google-notion_api
source venv/bin/activate
python --version  # Should be 3.12.x
pip list | grep -E "fastapi|notion|google"
```

### Verify ngrok:
```bash
ngrok version
ngrok config check
```

---

## 🏃 Step 6: Running the Servers

### Terminal 1: Main Backend
```bash
cd agent
./start.sh
# Or manually:
# source venv/bin/activate
# python -m uvicorn main:app --reload --port 8000
```

**Verify**: Visit http://localhost:8000/api/ping
Should see: `{"message":"pong"}`

### Terminal 2: ngrok
```bash
ngrok http 8000
```

**Copy the ngrok URL** (e.g., `https://xxxxx.ngrok-free.dev`)

### Terminal 3: Update Frontend Config
```bash
# Edit config.ts and update API_BASE_URL with your ngrok URL
# Example:
# export const API_BASE_URL = 'https://xxxxx.ngrok-free.dev';
```

### Terminal 4: Start Expo
```bash
npm start
# Or
npx expo start
```

**Then:**
- Press `i` for iOS simulator
- Press `a` for Android emulator
- Scan QR code with Expo Go app

---

## 🧪 Step 7: Testing the Connection

### Test Backend Locally:
```bash
curl http://localhost:8000/api/ping
# Expected: {"message":"pong"}
```

### Test Backend via ngrok:
```bash
curl -H "ngrok-skip-browser-warning: true" https://your-ngrok-url.ngrok-free.dev/api/ping
# Expected: {"message":"pong"}
```

### Test in Expo App:
1. Open the app in Expo
2. Check the connection status indicator
3. Look for "✅ Backend Connected" message
4. Check Expo console for logs

---

## 📝 Complete Package List Summary

### Frontend (npm):
```json
{
  "dependencies": {
    "@react-navigation/native": "^7.1.19",
    "@react-navigation/native-stack": "^7.6.2",
    "expo": "~54.0.23",
    "expo-status-bar": "~3.0.8",
    "nativewind": "^4.2.1",
    "prettier-plugin-tailwindcss": "^0.5.14",
    "react": "^19.1.0",
    "react-native": "0.81.5",
    "react-native-reanimated": "^4.1.3",
    "react-native-safe-area-context": "^5.4.0",
    "react-native-screens": "^4.18.0",
    "react-native-worklets": "^0.6.1",
    "react-native-worklets-core": "^1.6.2",
    "tailwindcss": "^3.4.18"
  },
  "devDependencies": {
    "@types/react": "~19.1.0",
    "babel-preset-expo": "^54.0.7",
    "typescript": "^5.9.2"
  }
}
```

### Main Backend (Python - agent/):
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### Google/Notion API Backend (Python - google-notion_api/):
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
python-dotenv>=1.0.0
httpx>=0.24.0
notion-client>=2.2.0
google-auth-oauthlib>=1.0.0
google-auth>=2.23.0
google-api-python-client>=2.100.0
```

### System Tools:
- Node.js (v18+)
- Python (3.10+, 3.12 recommended)
- ngrok
- Git

---

## 🔍 Troubleshooting

### Issue: "Command not found: python3.12"
**Solution**: Install Python 3.12 or use `python3` if 3.12 is your default

### Issue: "npm install fails"
**Solution**: 
```bash
rm -rf node_modules package-lock.json
npm install
```

### Issue: "Virtual environment not found"
**Solution**: 
```bash
cd agent  # or google-notion_api
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or install packages individually
```

### Issue: "ngrok authentication failed"
**Solution**: 
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN
```

### Issue: "Backend not connecting"
**Solution**:
1. Verify backend is running: `curl http://localhost:8000/api/ping`
2. Verify ngrok is running: Check http://localhost:4040
3. Update `config.ts` with correct ngrok URL
4. Check Expo console for errors

### Issue: "Port 8000 already in use"
**Solution**:
```bash
# Find and kill process
lsof -ti:8000 | xargs kill
# Or use a different port
```

---

## 📚 Quick Reference Commands

### Start Everything:
```bash
# Terminal 1: Backend
cd agent && ./start.sh

# Terminal 2: ngrok
ngrok http 8000

# Terminal 3: Expo
npm start
```

### Stop Everything:
```bash
# Stop backend
pkill -f "uvicorn main:app"

# Stop ngrok
pkill -f "ngrok http"

# Stop Expo (Ctrl+C in terminal)
```

### Check Status:
```bash
# Backend
curl http://localhost:8000/api/ping

# ngrok
curl http://localhost:4040/api/tunnels

# Check processes
ps aux | grep -E "uvicorn|ngrok|expo"
```

---

## ✅ Setup Checklist

- [ ] Node.js installed (v18+)
- [ ] Python 3.12 installed
- [ ] ngrok installed and authenticated
- [ ] Frontend dependencies installed (`npm install`)
- [ ] Main backend virtual environment created
- [ ] Main backend dependencies installed
- [ ] Google/Notion API virtual environment created
- [ ] Google/Notion API dependencies installed
- [ ] Environment variables configured (if needed)
- [ ] Backend server starts successfully
- [ ] ngrok tunnel established
- [ ] Frontend config.ts updated with ngrok URL
- [ ] Expo app connects to backend

---

## 📞 Need Help?

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all packages are installed correctly
3. Check server logs for error messages
4. Ensure all services are running on correct ports
5. Verify network connectivity

---

**Last Updated**: After Python 3.12 upgrade and virtual environment setup

