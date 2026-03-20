# lets build where we check inventory stock 

from langgraph.graph import StateGraph , START ,END
from typing import TypedDict


def process(state):
    state["count"] += 1
    return state


def decide(state):
    
    if state["Count"] >=3:
        
        return "finish"
    
    return "loop"


def finalize(state):
     print("Final result:", state["count"])
     return state
 

builder = StateGraph(dict) 

builder.add_node("process" , process)
builder.add_node("decide" , decide)
builder.add_node("final" , finalize)

builder.set_entry_point("process")
builder.add_edge("process", "decide")

builder.add_conditional_edges(
    "decide" ,
    decide ,
    
    {
        "loop" : "process",
        "finish" : "finialize"
    }
)
        
builder.add_edge("finalize", END)

graph = builder.compile()
        