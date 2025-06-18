from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """ Add two numbers """
    print("Addition is being done...")
    return a+b

@mcp.tool()
def multiple(a:int,b:int)-> int:
    """ Multiply two numbers """
    print("Multiplication is being done...")
    return a*b

#The transport="stdio" argument tells the server to:

#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.

if __name__=="__main__":
    mcp.run(transport="stdio")