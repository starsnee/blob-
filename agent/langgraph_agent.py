#from langgraph import Agent, Node, State
from langgraph.graph import StateGraph, START, END
import requests, os
from typing import TypedDict


# Define your state structure
class ChatState(TypedDict):
    prompt: str
    response: str

# Define your model call node
def call_model(state: ChatState):
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("NVIDIA_API_KEY")

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "meta/llama-3.1-nemotron-70b-instruct",
        "messages": [{"role": "user", "content": state["prompt"]}],
        "temperature": 0.7,
        "max_tokens": 512,
    }

    resp = requests.post(API_URL, headers=headers, json=payload)
    state["response"] = resp.json()["choices"][0]["message"]["content"]
    return state


# Define a second node (e.g., dummy tool)
def call_tools(state: ChatState):
    state["response"] += "\n\n[Tool checked ✅]"
    return state


# Build the LangGraph
graph = StateGraph(state_schema=ChatState)

graph.add_node("call_model", call_model)
graph.add_node("call_tools", call_tools)

graph.add_edge(START, "call_model")
graph.add_edge("call_model", "call_tools")
graph.add_edge("call_tools", END)

# Compile the workflow
compiled_agent = graph.compile()


# Helper function to run agent easily
def run_agent(prompt: str):
    state = {"prompt": prompt, "response": ""}
    final_state = compiled_agent.invoke(state)
    return final_state["response"]