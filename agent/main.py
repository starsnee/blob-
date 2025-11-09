"""
def main():
    print("Hello from blob!")


if __name__ == "__main__":
    main()
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests

# Create FastAPI app
app = FastAPI()

origins = [
    "http://localhost",  # For web-based testing if applicable
    "http://localhost:8081",  # Example for React Native development server
    # Add other origins if your React Native app might run on different IPs/ports
    # e.g., "http://192.168.1.100:8081" for a device on your local network
]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Test endpoint
@app.get("/api/ping")
async def ping():
    return {"message": "pong"}

# Health check
@app.get("/health")
async def health():
    return {"status": "ok"}

# -------------------------------
# NVIDIA Nemotron Chat Endpoint
# -------------------------------

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
API_KEY = os.getenv("NVIDIA_API_KEY")  # set via environment variable

class Prompt(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(data: Prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "meta/llama-3.1-nemotron-70b-instruct",
        "messages": [{"role": "user", "content": data.prompt}],
        "temperature": 0.7,
        "max_tokens": 512,
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return {"response": result["choices"][0]["message"]["content"]}
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)