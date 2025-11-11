# mcp-server-1

A simple Model Context Protocol (MCP) server that provides utilities to AI assistants, like Claude.
I'm using this repo to learn about MCP server implementation.

## MCP Framework
**MCP Python SDK** (`mcp` package)
_I considered using FastMCP framework which requires less boilerplate. I decided against it for this repo in hopes of more thoroughly internalizing concepts by using a more explicit framework._


## Development Approach

This project uses **PEP 723 inline dependency declarations** instead of a traditional project structure with `pyproject.toml` and lock files. This choice makes the server completely self-contained in a single file, which is ideal for:
- Learning and experimentation
- Easy sharing and portability
- Simple projects that don't need complex dependency management

For larger production projects, a traditional structure with `pyproject.toml`, lock files, and package structure would be more appropriate.


## Setup
This project uses [uv](https://github.com/astral-sh/uv) to run a self-contained Python script with inline dependencies ([PEP 723](https://peps.python.org/pep-0723/)).
This means that there is no installation required. Dependencies are declared inline in server.py, instead of in a pyproject.toml file.
```
# Clone the repository
git clone <repository-url>
cd mcp-server-1
```

##  Interacting with the MCP Server

1. Start the MCP Server
```
uv run ./server.py
```
The server will start and communicate via stdio (standard input/output), which is the standard transport for local MCP servers. 
The first time you run it, `uv` will automatically create a virtual environment and install the required dependencies.
_You may need to make the server.py file executable before running the above command._

2. Connect to the server via Claude Code
- Open claude code from the terminal.
- Enter `/mcp` to view available MCP servers. Confirm that `time-date-server` is one of them.

3. Exercise the server
- Resources can be referenced with @ mentions
- Tools will automatically be used during the conversation
- Prompts show up as / slash commands


## How It Works

1. The `server.py` file contains inline PEP 723 metadata declaring the `mcp` dependency
2. When Claude Desktop starts, it launches this MCP server as a subprocess using `uv run server.py`
3. `uv` automatically creates a virtual environment and installs dependencies on first run
4. The server advertises its available tools via the `tools/list` JSON-RPC method
5. During conversations, Claude can automatically call these tools when relevant
6. The server executes the requested tool and returns results to Claude
7. Claude incorporates the results into its response to you