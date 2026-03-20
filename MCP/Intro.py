# Model Context Protocol is a standard protocol that allow AI models to interact with external too , system and data sources

# Without MCP --> Ai only generate text 

# With MCP    User → AI → Tool → System → Result

# read files , query databases ,call APIs ,run code ,control services


"""  Core Componenet Of MCP 

1. MCP Client 

   -> MCP client live inside the AI application 
   -> Communication layer between AI Model  and MCP Server
   
   => Role 
       
       1. Connect with MCP Servers 
       2. Discovers available tools 
       3. Send tool request 
       4. Recieve tool request


-----------------------------------------------------------------------------------------

2. MCP SERVER 
   
   -> MCP server expose the tool ai can use
   -> Think like of tool provider
   
   
   Register tool as like 
   
   1. get weather()
   2. Send email()
   
------------------------------------------------------------------------------------------

3. Tools 

   
   -> Tools are the function that ai can use 
   
   -> They perform real action 
   
        get_user_orders(user_id)
        search_products(query)
        create_invoice(customer_id)           
        
    => Every tool has three important things 
    
      1. Tool name get_weather() 
      2. Tool description --> Get weather for  a specific city 
      3. Input schema 
          
          {
               city : string
          }    
   
   
   
   """