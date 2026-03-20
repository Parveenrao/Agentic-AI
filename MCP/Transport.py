"""  =>  Transport is the method to send message like  
        
          1. Tool discovery
          2. tool call
          3. tool result
     
      -> MCP support three transport 
         
         1. stdio 
         2. HTTP
         3. sockets


------------------------------------------------------------------------------------------

1. stdio Transport 
   
   -> standard input / standard ouput communication 
   
   -> This is used when server runs as a local process
   
   when stdio is used 
   
   1. MCP server runs locally
   2. tool interact with local files 
   3. tool control local system
   
   
   Client
     ↓
    stdio
     ↓
  MCP Server (local process)
     ↓
    Tools              
    
    
    Example ->  python server.py
    
    client connect using 
    
    stdio_client("python_server.py")
    
---------------------------------------------------------------------------------------------

2. HTTP Transport 
 
   -> HTTP transport is used when server runs remotely
   
       AI agent → cloud MCP server → tools
       
       User
        ↓
     AI Agent
        ↓
        HTTP
         ↓
   MCP Server (cloud)
         ↓
        Tools    
    
    


  









"""
