# Google & Notion API Integration

FastAPI backend for integrating Google Calendar and Notion.

## Setup

### 1. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

**Required Environment Variables:**

#### Notion OAuth:
- `NOTION_CLIENT_ID` - Your Notion OAuth client ID
- `NOTION_CLIENT_SECRET` - Your Notion OAuth client secret
- `NOTION_REDIRECT_URI` - OAuth redirect URI (e.g., `http://localhost:8000/auth/notion/callback`)
- `NOTION_ROOT_PAGE_ID` - Root page ID where projects will be created (optional, can use OAuth response)

#### Google OAuth:
- `GOOGLE_CLIENT_ID` - Your Google OAuth client ID
- `GOOGLE_CLIENT_SECRET` - Your Google OAuth client secret
- `GOOGLE_REDIRECT_URI` - OAuth redirect URI (e.g., `http://localhost:8000/auth/google/callback`)
- `GOOGLE_CALENDAR_ID` - Calendar ID (defaults to "primary")

### 3. Setting up OAuth Credentials

#### Notion:
1. Go to https://www.notion.so/my-integrations
2. Create a new integration
3. Copy the OAuth Client ID and Client Secret
4. Set the redirect URI in your integration settings

#### Google:
1. Go to https://console.cloud.google.com/apis/credentials
2. Create OAuth 2.0 Client ID credentials
3. Set authorized redirect URIs
4. Copy Client ID and Client Secret

## Running the Server

### Quick Start (Recommended):
```bash
cd google-notion_api
./start.sh
```

### Manual Start:
```bash
cd google-notion_api
source venv/bin/activate
python -m uvicorn GN_main:app --reload --port 8001
```

Or if running directly:

```bash
cd google-notion_api
source venv/bin/activate
python GN_main.py
```

**Note**: This project uses Python 3.12 in a virtual environment. The `start.sh` script automatically activates the venv.

The server will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Endpoints

### Authentication:
- `GET /auth/notion/login` - Initiate Notion OAuth flow
- `GET /auth/notion/callback` - Notion OAuth callback
- `GET /auth/google/login` - Initiate Google OAuth flow
- `GET /auth/google/callback` - Google OAuth callback

### Integration:
- `POST /integrations/notion/upsert_artifacts` - Create/update Notion pages with project artifacts
- `POST /integrations/calendar/create_event` - Create Google Calendar event

## Testing

Test environment variables:
```bash
python3 test_env.py
```

## Integration with Main Backend

To integrate this with your main backend (`agent/main.py`), you can:

1. Import the routes into your main app
2. Or run this as a separate service
3. Or merge the endpoints into `agent/main.py`

