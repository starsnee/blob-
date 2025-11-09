# Setup Checklist for Google-Notion API

## ✅ Issues Fixed

1. **Relative imports** - Changed from `from . import` to absolute imports
2. **Naming conflict** - Renamed `google.py` to `google_helpers.py` (conflicted with `google` package)
3. **Python 3.9 compatibility** - Changed `str|None` to `Optional[str]` for type hints
4. **Missing dependencies** - Created `requirements.txt` with all required packages
5. **Missing documentation** - Created README.md with setup instructions

## 📦 Dependencies Installed

All dependencies have been installed in Python 3.12 virtual environments:
- ✅ fastapi
- ✅ uvicorn
- ✅ pydantic
- ✅ python-dotenv
- ✅ httpx
- ✅ notion-client
- ✅ google-auth-oauthlib
- ✅ google-auth
- ✅ google-api-python-client

**Python Version**: Upgraded to Python 3.12 (from 3.9)
- Virtual environments created in both `agent/venv` and `google-notion_api/venv`
- All dependencies installed with Python 3.12
- No more importlib.metadata errors
- No more Python version warnings

## ⚠️ Still Needed

### 1. Environment Variables (.env file)

Create a `.env` file in the `google-notion_api` directory with:

```env
# Notion OAuth
NOTION_CLIENT_ID=your_notion_client_id
NOTION_CLIENT_SECRET=your_notion_client_secret
NOTION_REDIRECT_URI=http://localhost:8000/auth/notion/callback
NOTION_ROOT_PAGE_ID=your_notion_root_page_id

# Google OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
GOOGLE_CALENDAR_ID=primary
```

### 2. OAuth Credentials Setup

#### Notion:
1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Create OAuth integration (not Internal integration)
4. Copy Client ID and Client Secret
5. Set redirect URI in integration settings

#### Google:
1. Go to https://console.cloud.google.com/apis/credentials
2. Create OAuth 2.0 Client ID
3. Set application type to "Web application"
4. Add authorized redirect URI: `http://localhost:8000/auth/google/callback`
5. Copy Client ID and Client Secret

### 3. Port Conflict

⚠️ **Important**: This service runs on port 8000, which conflicts with your main backend (`agent/main.py`).

**Options:**
- Run on a different port: `python3 -m uvicorn GN_main:app --reload --port 8001`
- Merge endpoints into `agent/main.py`
- Use a reverse proxy/load balancer

## 🚀 Running the Server

```bash
cd google-notion_api
python3 -m uvicorn GN_main:app --reload --port 8001
```

Or directly:
```bash
python3 GN_main.py
```

## 🧪 Testing

1. Test environment variables:
```bash
python3 test_env.py
```

2. Check if server starts:
```bash
python3 GN_main.py
```

3. Visit API docs: http://localhost:8001/docs

## 📝 Notes

- The code uses an in-memory user store (`USER` dict) - this should be replaced with a database for production
- Python 3.9 warnings are non-critical but consider upgrading to Python 3.10+ for better compatibility
- OpenSSL warnings are also non-critical for development

