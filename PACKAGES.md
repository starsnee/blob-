# Package Dependencies - Quick Reference

## 📦 Frontend Dependencies (npm)

### Installation:
```bash
npm install
```

### Production Packages:
- `@react-navigation/native@^7.1.19`
- `@react-navigation/native-stack@^7.6.2`
- `expo@~54.0.23`
- `expo-status-bar@~3.0.8`
- `nativewind@^4.2.1`
- `prettier-plugin-tailwindcss@^0.5.14`
- `react@^19.1.0`
- `react-native@0.81.5`
- `react-native-reanimated@^4.1.3`
- `react-native-safe-area-context@^5.4.0`
- `react-native-screens@^4.18.0`
- `react-native-worklets@^0.6.1`
- `react-native-worklets-core@^1.6.2`
- `tailwindcss@^3.4.18`

### Development Packages:
- `@types/react@~19.1.0`
- `babel-preset-expo@^54.0.7`
- `typescript@~5.9.2`

---

## 🐍 Main Backend Dependencies (Python - agent/)

### Installation:
```bash
cd agent
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Packages (requirements.txt):
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
pydantic>=2.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

### Individual Install:
```bash
pip install fastapi 'uvicorn[standard]' pydantic requests python-dotenv
```

---

## 🐍 Google/Notion API Dependencies (Python - google-notion_api/)

### Installation:
```bash
cd google-notion_api
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Packages (requirements.txt):
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

---

## 🛠️ System Dependencies

### Required:
- **Node.js**: v18+ (includes npm)
- **Python**: 3.10+ (3.12 recommended)
- **ngrok**: For exposing backend to mobile
- **Git**: For version control

### Installation:

**macOS (Homebrew):**
```bash
brew install node python@3.12 ngrok/ngrok/ngrok
```

**Linux (Ubuntu/Debian):**
```bash
# Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Python 3.12
sudo apt install -y python3.12 python3.12-venv python3-pip

# ngrok
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok
```

**Windows:**
- Download Node.js from https://nodejs.org/
- Download Python from https://www.python.org/downloads/
- Download ngrok from https://ngrok.com/download

---

## ✅ Verification Commands

### Frontend:
```bash
node --version        # Should be v18+
npm list --depth=0    # List installed packages
```

### Main Backend:
```bash
cd agent
source venv/bin/activate
python --version      # Should be 3.12.x
pip list              # List installed packages
```

### Google/Notion API Backend:
```bash
cd google-notion_api
source venv/bin/activate
python --version      # Should be 3.12.x
pip list              # List installed packages
```

### System Tools:
```bash
node --version
python3.12 --version
ngrok version
git --version
```

---

## 📋 Complete Installation Checklist

### Frontend:
- [ ] `npm install` completed
- [ ] All packages in `package.json` installed
- [ ] TypeScript compiles without errors

### Main Backend:
- [ ] Virtual environment created (`agent/venv/`)
- [ ] Dependencies installed from `requirements.txt`
- [ ] Server starts with `./start.sh`

### Google/Notion API Backend:
- [ ] Virtual environment created (`google-notion_api/venv/`)
- [ ] Dependencies installed from `requirements.txt`
- [ ] Server starts with `./start.sh`

### System:
- [ ] Node.js v18+ installed
- [ ] Python 3.12 installed
- [ ] ngrok installed and authenticated
- [ ] Git installed

---

## 🔄 Reinstalling Dependencies

### Frontend:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Main Backend:
```bash
cd agent
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Google/Notion API Backend:
```bash
cd google-notion_api
rm -rf venv
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

**See `SETUP_GUIDE.md` for detailed setup instructions.**

