# how system remember past interations , state , context 


# 1. Short term memory --> the state object that flows through your graph during execution , it is temporay , process memory

from typing import TypedDict , Optional , List
from langchain_core.messages import BaseMessage

class State(TypedDict):
    message : List[BaseMessage]
    user_input :str          
    intent : str          
    response : str             
    
"""Initial State
   ↓
Node 1 (adds user_input)
   ↓
Node 2 (detects intent)
   ↓
Node 3 (generates response)
   ↓
Final State"""    



""" Goal: Smart AI Assistant with State

We'll build an agent that:

Takes user input

Detects intent

Calls a tool (mock)

Generates response

Maintains conversation memory         """


from typing import TypedDict, List, Optional
from langchain_core.messages import BaseMessage
from typing_extensions import Annotated
from operator import add


class State(TypedDict):
    messages: Annotated[List[BaseMessage], add]  # auto-append
    user_input: str
    intent: Optional[str]
    tool_result: Optional[str]
    response: Optional[str]
    
    
# Node 1 input node    
def input_node(state: State):
    return {
        "messages": [{"role": "user", "content": state["user_input"]}]
    }
    
# Node 2 intent 

def detect_intent(state: State):
    text = state["user_input"].lower()

    if "weather" in text:
        intent = "get_weather"
    elif "time" in text:
        intent = "get_time"
    else:
        intent = "chat"

    return {"intent": intent}


# Node 3 tool node 

def tool_node(state: State):
    intent = state["intent"]

    if intent == "get_weather":
        result = "Weather is 25°C"
    elif intent == "get_time":
        result = "Current time is 10:30 AM"
    else:
        result = None

    return {"tool_result": result}

# node 3 response node 

def response_node(state: State):
    if state["tool_result"]:
        reply = f"Here is the info: {state['tool_result']}"
    else:
        reply = "I can help with weather or time."

    return {
        "response": reply,
        "messages": [{"role": "assistant", "content": reply}]
    }
    
# Routing logic 

def route(state: State):
    if state["intent"] in ["get_weather", "get_time"]:
        return "tool"
    return "response"


from langgraph.graph import StateGraph, END

builder = StateGraph(State)

builder.add_node("input", input_node)
builder.add_node("intent", detect_intent)
builder.add_node("tool", tool_node)
builder.add_node("response", response_node)

builder.set_entry_point("input")

builder.add_edge("input", "intent")
builder.add_conditional_edges("intent", route, {
    "tool": "tool",
    "response": "response"
})

builder.add_edge("tool", "response")
builder.add_edge("response", END)

graph = builder.compile()        



result = graph.invoke({
    "user_input": "What is the weather?"
})

print(result["response"])

#---------------------------------------------------------------------------------------------------------------------

# Long term memory 


from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)           # checkpoint memory 

# All users share memory ❌ (disaster)


# Sematic memory 

""" Semantic Memory (RAG)

This is where real systems shine.

Instead of storing raw chat:

👉 Store meaning (embeddings)

Use:

FAISS

Chroma    








          ┌──────────────┐
          │   User Input │
          └──────┬───────┘
                 ↓
        ┌──────────────────┐
        │ Short-term State │
        └──────┬───────────┘
               ↓
     ┌──────────────────────┐
     │ Retrieve Long Memory │
     │ (Vector DB / SQL)    │
     └──────┬───────────────┘
            ↓
        ┌────────────┐
        │   LLM Call │
        └────┬───────┘
             ↓
   ┌────────────────────┐
   │ Save to Memory     │
   │ (Checkpoint + DB)  │
   └────────────────────┘"""


from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "user_1"}}

# First call
graph.invoke({
    "messages": [{"role": "user", "content": "Hi"}]
}, config=config)

# Second call (memory persists)
graph.invoke({
    "messages": [{"role": "user", "content": "What did I say?"}]
}, config=config)