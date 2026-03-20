from mcp.server.fastmcp import FastMCP
import mcp

# create the name and give it to name 

mcp = FastMCP("my-first-server")

# define a tool 

@mcp.tool()
def  say_hello(name : str) -> str:
    
    return f" HEllo : {name}"



if __name__ == "__main__":
    mcp.run()