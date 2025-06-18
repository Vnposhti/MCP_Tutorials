import streamlit as st
import asyncio
import platform

# Windows event loop compatibility
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from dotenv import load_dotenv
load_dotenv()

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

st.set_page_config(page_title="MCP_Tutorial", page_icon="🧠")
st.title('🤖 MCP: Math & Search Assistant')

st.markdown("""
This app demonstrates the use of MCP to create an agent with both Math and Search capabilities.
The agent is able to perform basic arithmetic and retrieve information from an external search engine.
""")

query = st.text_area("Enter your query:", placeholder="e.g. (3 + 5) * 12 or What is LLM?")

async def setup_agent():
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["mathserver.py"],
            "transport": "stdio",
        },
        "search": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    })

    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)
    return agent

async def main_app():
    agent = await setup_agent()

    if st.button("Response") and query.strip():
        with st.spinner("Invoking tools via MCP..."):
            response = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})
            content = response['messages'][-1].content if 'messages' in response else str(response)
            st.markdown("#### 🤖 Agent Response:")
            st.markdown(content)

asyncio.run(main_app())