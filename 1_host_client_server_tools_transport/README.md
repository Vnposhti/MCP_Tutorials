# 🤖 MCP (Model Context Protocol) Agent Demo with LangChain, Math, and Search Tools

This project demonstrates how to build an **MCP-powered Agent** that can:
- 🧠 Perform arithmetic operations via a local `mathserver`
- 🌐 Search the web using a Tavily-powered `searchserver`
- 💬 Be interacted with via a CLI or a user-friendly Streamlit frontend

But more importantly, it explains the **underlying architecture of MCP**, the types of transports it supports, and how tool execution is decoupled and distributed.

---

## 📘 What is MCP?

**MCP (Model Context Protocol)** is a specification for building interoperable toolchains that agents can communicate with across local or remote environments. It was introduced by LangChain to help agents access tools that may be hosted:
- In other processes
- On different machines
- Across different protocols

The key idea is to **standardize the way tools are defined and invoked**, regardless of where or how they’re hosted.

---

## 🏗️ MCP Architecture Components
image.png

### ✅ MCP Host
An environment (often a server or local machine) that serves or executes the tools.

### ✅ MCP Server
A script/app exposing a set of tools to the agent, registered via the `@mcp.tool()` decorator. It uses a transport mechanism to communicate (e.g., HTTP or stdio).

### ✅ MCP Client
The agent or application that connects to one or more MCP Servers and accesses tools remotely.

### ✅ MCP Transport
Defines how messages (tool invocation requests/responses) are sent between clients and servers.

### Supported Transports:
| Type         | Description                                          | Example Use Case        |
|--------------|------------------------------------------------------|--------------------------|
| `stdio`      | Uses standard input/output for communication         | Local CLI-based tools    |
| `streamable-http` (HTTP-SSE) | Uses HTTP + Server-Sent Events to support streaming | Remote API tools         |

## 🚀 Project Architecture

                        +------------------+
                        |     Agent        |
                        | (LangChain/Groq) |
                        +------------------+
                                |
                                | Uses
                        +------------------+
                        | MultiServerMCP   |
                        +------------------+
                         /              \\
                (stdio/local)         (HTTP/SSE)
                mathserver.py          search.py

- `mathserver.py`: Implements math tools and communicates over **stdio**
- `search.py`: Implements search tools and serves via **streamable HTTP**
- `client.py`: Agent script that uses both servers
- `app.py`: Streamlit frontend

---

## 🚀 Running the Project

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run Math Server
```bash
python mathserver.py
```
### 3. Run Search Server
```bash
python search.py
```

### 4. Run the client
```bash
python client.py
```

### 5 Launch the Streamlit App
```bash
streamlit run app.py
```