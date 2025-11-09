import os, base64
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from notion_client import Client

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

def make_notion_client(user_token: Optional[str] = None) -> Client:
    """
    If you're doing user OAuth, pass that user's access_token here.
    For quick internal testing you can set NOTION_TOKEN in .env and call without args.
    """
    token = user_token or os.getenv("NOTION_TOKEN")
    if not token:
        raise RuntimeError("No Notion token provided")
    return Client(auth=token)

def _rich(t: str) -> List[Dict[str, Any]]:
    return [{"type": "text", "text": {"content": t[:2000]}}] if t else []

def _title(t: str) -> List[Dict[str, Any]]:
    return [{"type": "text", "text": {"content": t[:200]}}]

def ensure_project_page(notion: Client, root_page_id: str, project_name: str, description: str = "") -> str:
    page = notion.pages.create(
        parent={"type":"page_id","page_id":root_page_id},
        properties={"title":{"title":_title(project_name)}},
        children=[
            {"object":"block","type":"heading_2","heading_2":{"rich_text":_rich("Overview")}},
            {"object":"block","type":"paragraph","paragraph":{"rich_text":_rich(description)}},
        ],
    )
    return page["id"]

def ensure_db(notion: Client, parent_page_id: str, title: str, props: Dict[str, Any]) -> str:
    db = notion.databases.create(
        parent={"type":"page_id","page_id":parent_page_id},
        title=[{"type":"text","text":{"content":title}}],
        properties=props,
    )
    return db["id"]

def upsert_bundle(notion: Client, root_page_id: str, bundle: Dict[str, Any]) -> Dict[str, Any]:
    page_id = ensure_project_page(notion, root_page_id, bundle["project_name"], bundle.get("description",""))

    okr_db = ensure_db(notion, page_id, "OKRs", {
        "Name":{"title":{}}, "Owner":{"rich_text":{}}, "Metric":{"rich_text":{}},
        "Target":{"rich_text":{}}, "Due":{"date":{}}, "Objective":{"rich_text":{}}
    })
    roadmap_db = ensure_db(notion, page_id, "Roadmap (Epics)", {
        "Name":{"title":{}}, "Problem":{"rich_text":{}}, "Scope":{"rich_text":{}},
        "Dependencies":{"rich_text":{}}, "Release Target":{"date":{}}, "Risk":{"rich_text":{}}
    })
    backlog_db = ensure_db(notion, page_id, "Backlog (Stories)", {
        "Name":{"title":{}}, "As a":{"rich_text":{}}, "I want":{"rich_text":{}}, "So that":{"rich_text":{}},
        "Acceptance Criteria":{"rich_text":{}}, "Effort":{"number":{"format":"number"}},
        "Priority":{"select":{"options":[{"name":"Must"},{"name":"Should"},{"name":"Could"}]}}, "Due":{"date":{}}
    })
    notes_db = ensure_db(notion, page_id, "Notes", {"Name":{"title":{}}, "Summary":{"rich_text":{}}})

    # Insert content
    for okr in bundle.get("okrs", []):
        obj = okr["objective"]
        for kr in okr.get("key_results", []):
            notion.pages.create(parent={"database_id": okr_db}, properties={
                "Name":{"title":_title(kr.get("title","KR"))},
                "Objective":{"rich_text":_rich(obj)},
                "Owner":{"rich_text":_rich(kr.get("owner",""))},
                "Metric":{"rich_text":_rich(kr.get("metric",""))},
                "Target":{"rich_text":_rich(kr.get("target",""))},
                "Due":{"date":{"start":kr.get("due")}} if kr.get("due") else None
            })
    for e in bundle.get("roadmap", []):
        notion.pages.create(parent={"database_id": roadmap_db}, properties={
            "Name":{"title":_title(e["title"])},
            "Problem":{"rich_text":_rich(e.get("problem",""))},
            "Scope":{"rich_text":_rich(e.get("scope",""))},
            "Dependencies":{"rich_text":_rich(", ".join(e.get("dependencies",[])))},
            "Release Target":{"date":{"start":e.get("release_target")}} if e.get("release_target") else None,
            "Risk":{"rich_text":_rich(e.get("risk",""))},
        })
    for s in bundle.get("backlog", []):
        notion.pages.create(parent={"database_id": backlog_db}, properties={
            "Name":{"title":_title(s["title"])},
            "As a":{"rich_text":_rich(s.get("as_a",""))},
            "I want":{"rich_text":_rich(s.get("i_want",""))},
            "So that":{"rich_text":_rich(s.get("so_that",""))},
            "Acceptance Criteria":{"rich_text":_rich("\n".join(s.get("acceptance_criteria",[])))},
            "Effort":{"number":s.get("effort")} if s.get("effort") is not None else None,
            "Priority":{"select":{"name":s.get("priority")}} if s.get("priority") else None,
            "Due":{"date":{"start":s.get("due")}} if s.get("due") else None,
        })
    if bundle.get("notes_summary"):
        notion.pages.create(parent={"database_id": notes_db},
                           properties={"Name":{"title":_title("Latest Meeting Summary")},
                                       "Summary":{"rich_text":_rich(bundle["notes_summary"])}})

    return {"project_page_id": page_id, "dbs":{"okrs":okr_db,"roadmap":roadmap_db,"backlog":backlog_db,"notes":notes_db}}
