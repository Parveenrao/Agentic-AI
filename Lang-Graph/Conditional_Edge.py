# Conditional edge decide which node to go to next based on state 

from typing import TypedDict


from langgraph.graph import StateGraph , START , END

class State(TypedDict):   # state is the data shared across node 
    number : int          
    
    
# create node

def check_number(state):
    return state


def even_node(state):
    print("Number is even")
    return state

def odd_node(state):
    print("Number is odd")
    return state


# conditionn function 

def route(state):
    if state["number"] % 2 == 0:
        return "even"
    
    else:
        return "odd"    
    

# Build graph

builder = StateGraph(State)


builder.add_node("check" , check_number)
builder.add_node("even" , even_node)
builder.add_node("odd" , odd_node)

builder.set_entry_point("check") 

builder.add_conditional_edges("check" ,
             route,
             
             {
                 "even" : "even",
                 "odd" : "odd"
             }
                              )   

builder.add_edge("even", END)
builder.add_edge("odd", END)

graph = builder.compile()    

