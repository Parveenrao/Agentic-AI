from typing import TypedDict , List
from langgraph.graph import StateGraph  , START , END

import warnings
warnings.filterwarnings("ignore")



#First state ->state is the data that shared across the worflows, each node reads and updat the state, think like memory of workflow

class BlogState(TypedDict):
    topic : str              # input - never change  , topic is the only key you set at first
    title : str              # set by generate_title  node
    intro : str              # set by write intro node
    bullets : List[str]      # set by add_bullets node
    post : str               # set by final post


# 2nd state , Node -> Node is the function that do work, each function recieve full state but only return key its owns

def generate_title(state : BlogState) -> dict:
    topic = state["topic"]
    title = f" The Complete guide to {topic} " 
    
    return {
        "title" : title
    }   
    
    
def write_intro(state : BlogState) -> dict:
    
    title = state["title"]   # set by previous node
    
    intro = (
        
        f"Welcome to {title}"
        "In this post we cover everthing you need to know"
    )
    
    return {"intro" : intro}


def add_bullets(state: BlogState) -> dict:
    topic = state["topic"]
    bullets = [
        f"What is {topic} and why it matters",
        f"Core concepts of {topic}",
        f"How to get started with {topic}",
        f"Common mistakes when learning {topic}",
        f"Next steps after mastering {topic}",
    ]
    return {"bullets": bullets}


def add_cta(state: BlogState) -> dict:
    # This node reads from ALL previous nodes to assemble the post
    bullet_text = "\n".join(f"  - {b}" for b in state["bullets"])
    post = (
        f"# {state['title']}\n\n"
        f"{state['intro']}\n\n"
        f"## What you'll learn\n{bullet_text}\n\n"
        "## Ready to start?\n"
        "Drop your questions in the comments below!"
    )


#3rd state , Edge -> decide which node run next 

builder = StateGraph(BlogState)


builder.add_node("generate_title", generate_title)
builder.add_node("write_intro",    write_intro)
builder.add_node("add_bullets",    add_bullets)
builder.add_node("add_cta",        add_cta)


builder.add_edge(START , "generate_title")
builder.add_edge("generate_title" ,  "write_intro")
builder.add_edge("write_intro" , "add_bullets")
builder.add_edge("add_bullets" , "add_cta")
builder.add_edge("add_cta" , END)


#4th state , Graph - > connect everything , state --> node --> edge = graph 

graph = builder.compile()

# Run it
result = graph.invoke({
    "topic":   "LangGraph",
    "title":   "",
    "intro":   "",
    "bullets": [],
    "post":    "",
})

print(result["post"])

graph.invoke({"number": 4})


