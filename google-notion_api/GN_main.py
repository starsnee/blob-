import os, base64, json
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import httpx

from notion_client import Client
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

import notion as notion_helpers
import google_helpers

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

app = FastAPI(title="Blob Integrations API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=False)

# ---- Simple in-memory token store for demo (replace with DB) ----
USER = {"email":"demo@blob.app", "notion_token":None, "notion_root":None,
        "google_refresh":None, "google_access":None}

# ===================== Notion OAuth ==============================
NOTION_CLIENT_ID = os.getenv("NOTION_CLIENT_ID")
NOTION_CLIENT_SECRET = os.getenv("NOTION_CLIENT_SECRET")
NOTION_REDIRECT_URI = os.getenv("NOTION_REDIRECT_URI")

@app.get("/auth/notion/login")
def notion_login():
    url = (
        "https://api.notion.com/v1/oauth/authorize"
        f"?client_id={NOTION_CLIENT_ID}&response_type=code&owner=user&redirect_uri={NOTION_REDIRECT_URI}"
    )
    return RedirectResponse(url)

@app.get("/auth/notion/callback")
async def notion_callback(code: str = ""):
    if not code: raise HTTPException(400, "Missing code")
    basic = base64.b64encode(f"{NOTION_CLIENT_ID}:{NOTION_CLIENT_SECRET}".encode()).decode()
    payload = {"grant_type":"authorization_code","code":code,"redirect_uri":NOTION_REDIRECT_URI}
    async with httpx.AsyncClient() as client:
        resp = await client.post("https://api.notion.com/v1/oauth/token",
                                 headers={"Authorization": f"Basic {basic}","Content-Type":"application/json"},
                                 json=payload)
    data = resp.json()
    if resp.status_code >= 300: raise HTTPException(resp.status_code, str(data))
    USER["notion_token"] = data["access_token"]
    USER["notion_root"]  = data.get("duplicated_template_id") or os.getenv("NOTION_ROOT_PAGE_ID")
    return {"ok": True, "workspace": data.get("workspace_name")}

# ===================== Google OAuth ==============================
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def _flow():
    return Flow.from_client_config(
        {"web": {"client_id": GOOGLE_CLIENT_ID,
                 "project_id": "blob-hack",
                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                 "token_uri": "https://oauth2.googleapis.com/token",
                 "client_secret": GOOGLE_CLIENT_SECRET,
                 "redirect_uris": [GOOGLE_REDIRECT_URI]}},
        scopes=SCOPES, redirect_uri=GOOGLE_REDIRECT_URI)

@app.get("/auth/google/login")
def google_login():
    flow = _flow()
    url, state = flow.authorization_url(access_type="offline", include_granted_scopes="true", prompt="consent")
    return RedirectResponse(url)

@app.get("/auth/google/callback")
def google_callback(code: str = "", state: str = ""):
    flow = _flow()
    flow.fetch_token(code=code)
    creds: Credentials = flow.credentials
    USER["google_refresh"] = creds.refresh_token
    USER["google_access"] = creds.token
    return {"ok": True, "has_refresh_token": bool(creds.refresh_token)}

# ===================== Contracts & Integration routes ============
class KeyResult(BaseModel):
    title: str
    metric: Optional[str] = None
    target: Optional[str] = None
    owner: Optional[str] = None
    due: Optional[str] = None

class OKR(BaseModel):
    objective: str
    key_results: List[KeyResult] = []

class Story(BaseModel):
    title: str
    as_a: Optional[str] = None
    i_want: Optional[str] = None
    so_that: Optional[str] = None
    acceptance_criteria: List[str] = []
    effort: Optional[int] = None
    priority: Optional[str] = None
    due: Optional[str] = None

class Epic(BaseModel):
    title: str
    problem: Optional[str] = None
    scope: Optional[str] = None
    dependencies: List[str] = []
    release_target: Optional[str] = None
    risk: Optional[str] = None

class ArtifactBundle(BaseModel):
    project_name: str
    description: Optional[str] = None
    okrs: List[OKR] = []
    roadmap: List[Epic] = []
    backlog: List[Story] = []
    notes_summary: Optional[str] = None

class CalendarEvent(BaseModel):
    summary: str
    description: Optional[str] = None
    start_iso: str
    end_iso: str
    attendees: List[str] = []
    conference: bool = False

@app.post("/integrations/notion/upsert_artifacts")
def upsert_artifacts(bundle: ArtifactBundle):
    token = USER["notion_token"] or os.getenv("NOTION_TOKEN")
    root  = USER["notion_root"]  or os.getenv("NOTION_ROOT_PAGE_ID")
    if not token or not root:
        raise HTTPException(400, "Connect Notion first or provide NOTION_TOKEN/NOTION_ROOT_PAGE_ID.")
    client = Client(auth=token)
    result = notion_helpers.upsert_bundle(client, root, bundle.dict())
    return {"ok": True, "result": result}

@app.post("/integrations/calendar/create_event")
def calendar_create(evt: CalendarEvent):
    refresh = USER["google_refresh"]
    if not refresh:
        raise HTTPException(400, "Connect Google first.")
    service = google_helpers.svc_from_tokens(access_token=USER["google_access"], refresh_token=refresh)
    created = google_helpers.create_event(service, evt.summary, evt.description or "",
                                          evt.start_iso, evt.end_iso, evt.attendees, evt.conference)
    return {"ok": True, "event": created}

"""
cd blob-/notion_google_API
uvicorn main:app --reload
# open http://127.0.0.1:8000/docs

"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port="8000")