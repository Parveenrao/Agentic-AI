# Lang-Graph is a framework to build ai agents using graph workflows

"""   => Instead of running steps in a straight line, it uses a graph (nodes + edges) so the AI can:

            make decisions --> loop tasks -> call tools -> maintain memory -> coordinate multiple agents
            
            
            
            
            
        => Workflow 
        
        
        
        
        ┌─────────┐
        │  User   │
        └────┬────┘
             │
        ┌────▼────┐
        │  Agent  │
        └────┬────┘
             │
     ┌───────▼────────┐
     │ Tool / Search  │
     └───────┬────────┘
             │
        ┌────▼────┐
        │  Memory │
        └────┬────┘
             │
        ┌────▼────┐
        │ Response│
        └─────────┘    
            
            """