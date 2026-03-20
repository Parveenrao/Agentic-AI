from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Utilty Server")

@mcp.tool()
def add(a : int , b : int) -> int:  
    # add two numbers
    return a + b

@mcp.tool()
def multiply(a : int , b : int) -> int: 
    # multiply weather 
    
    return a * b   

@mcp.tool()
def greet(name : str) -> str:     
    " greet a user"
    
    return f"Hello {name} , welcome"

@mcp.tool()
def weather(city : str) -> str :
    # weather of a particular city 
    
    return f" weather of this {city} is 27 c"


if __name__ == "__main__":
    mcp.run()