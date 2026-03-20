# Sometimes ai could not reach the final steps , so a human must approve it or correct it 

from langgraph.graph import StateGraph , START , END
from typing import TypedDict


class DonationState(TypedDict):
    item : str        
    risk : bool       
    approved : bool
    
# Ai analyze the item 

# Node 1 AI analysis

def ai_analysis(state):
    print("Ai analyze the item" , state["item"])
    
    if state["item"] == "laptop":
        state["risk"] = True
    
    else:
        state["risk"] = False

# Node 2 Risk decison 

def risk_decision(state):
    
    if state["risk"]:
        return "review"
    
    return "Execute"


def human_review(state):
    print("Admin reviewing request")
    
    state["approved"] = True
    
    return state

# Step 4: Execute transfer
def execute_transfer(state):
    print("Transfer approved and executed")
    return state


builder = StateGraph(DonationState)

builder.add_node("ai_analysis", ai_analysis)
builder.add_node("human_review", human_review)
builder.add_node("execute_transfer", execute_transfer)

builder.set_entry_point("ai_analysis")

builder.add_conditional_edges(
    "ai_analysis",
    risk_decision,
    {
        "review": "human_review",
        "execute": "execute_transfer"
    }
)

builder.add_edge("human_review", "execute_transfer")
builder.add_edge("execute_transfer", END)

graph = builder.compile()

graph.invoke({
    "item": "laptop",
    "risk": False,
    "approved": False
})