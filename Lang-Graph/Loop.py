# A loop happens when graph route to prevoius node to previous node instead  of moving forward to END.

from langgraph.graph import StateGraph , START , END
from typing import TypedDict


class AgentState(TypedDict):
    count : str               
    

# Node 1

def increment(state):
    state["count"] += 1
    print("Current count" , state["count"])
    return state

# Node 2

def check(state):
    if state["count"] >= 3:
        return "End"
    
    return "loop"

builder  = StateGraph(AgentState)

builder.add_node("increment" , increment)
builder.add_node("decision_node" , check)

builder.set_entry_point("increment")

builder.add_edge("increment", "check")

builder.add_conditional_edges(
    "check",
    lambda state: check(state),
    {
        "loop": "increment",
        "end": END
    }
)

graph = builder.compile()

graph.invoke({"count": 0})
  
            