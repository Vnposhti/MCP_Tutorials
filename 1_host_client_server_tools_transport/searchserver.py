from dotenv import load_dotenv
load_dotenv()

from mcp.server.fastmcp import FastMCP
from langchain_tavily import TavilySearch

tavily = TavilySearch()
mcp=FastMCP("Tavily Search Engine")

@mcp.tool()
async def search_query(input:str)->str:
    """Return the top 5 search result summaries based on user query input using Tavily."""
    print("Searching for result using Tavily...")
    result = await tavily.ainvoke({"query": input})
    results = result.get("results", [])

    output = ""
    for i, r in enumerate(results[:5], 1):
        title = r.get("title", "No title")
        content = r.get("content", "No content")
        url = r.get("url", "")
        output += f"🔹 **Result {i}: {title}**\n{content}\n🔗 {url}\n\n"

    return output.strip()

if __name__=="__main__":
    mcp.run(transport="streamable-http")