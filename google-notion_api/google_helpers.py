import os
from typing import List
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID","primary")

def svc_from_tokens(access_token: str = None, refresh_token: str = None,
                    client_id: str = None, client_secret: str = None):
    creds = Credentials(
        token=access_token, refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id or os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=client_secret or os.getenv("GOOGLE_CLIENT_SECRET"),
        scopes=SCOPES,
    )
    return build("calendar", "v3", credentials=creds, cache_discovery=False)

def create_event(service, summary: str, description: str, start_iso: str, end_iso: str,
                 attendees: List[str], conference: bool=False) -> dict:
    body = {
        "summary": summary,
        "description": description or "",
        "start": {"dateTime": start_iso},
        "end": {"dateTime": end_iso},
        "attendees": [{"email": a} for a in attendees] if attendees else [],
    }
    if conference:
        body["conferenceData"] = {"createRequest": {"requestId": summary.replace(" ","-")}}
    event = service.events().insert(
        calendarId=CALENDAR_ID, body=body,
        conferenceDataVersion=1 if conference else 0
    ).execute()
    return {"id": event.get("id"), "htmlLink": event.get("htmlLink"), "hangoutLink": event.get("hangoutLink")}
