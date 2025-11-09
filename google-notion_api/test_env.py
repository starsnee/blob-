import os
from dotenv import load_dotenv

load_dotenv()

print("Client ID:", os.getenv("NOTION_CLIENT_ID"))
print("Client Secret:", os.getenv("NOTION_CLIENT_SECRET"))
print("Redirect URI:", os.getenv("NOTION_REDIRECT_URI"))