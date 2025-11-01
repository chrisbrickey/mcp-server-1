# mcp-server-1

A simple Model Context Protocol (MCP) server that provides utilities to AI assistants, like Claude.
I'm using this repo to learn about MCP server implementation.

## MCP Framework

- **MCP Python SDK** (`mcp` package)
_I considered using FastMCP framework which requires less boilerplate. I decided against it for this repo in hopes of more thoroughly internalizing concepts by using a more explicit framework._

## Features

This MCP server provides the following tools at this time:
- fetch current date

## Installation

This project uses [uv](https://github.com/astral-sh/uv) to run a self-contained Python script with inline dependencies ([PEP 723](https://peps.python.org/pep-0723/)).

```bash
# Clone the repository
git clone <repository-url>
cd mcp-server-1

# No installation needed! Dependencies are declared inline in server.py instead of in a pyproject.toml file.
```

## Usage

### Running the Server

```bash
# Run the MCP server (uv handles dependencies automatically)
uv run ./server.py
```
_You may need to make the server.py file executable before running the above command._

The server will start and communicate via stdio (standard input/output), which is the standard transport for local MCP servers. The first time you run it, `uv` will automatically create a virtual environment and install the required dependencies.

### Connecting to Claude Desktop

To use this server with Claude Desktop, add it to your Claude Desktop configuration file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "time-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-server-1",
        "run",
        "server.py"
      ]
    }
  }
}
```

Replace `/absolute/path/to/mcp-server-1` with the actual path to this project directory.

After updating the configuration, restart Claude Desktop. The time and date tools will be automatically available during your conversations with Claude.


## How It Works

1. The `server.py` file contains inline PEP 723 metadata declaring the `mcp` dependency
2. When Claude Desktop starts, it launches this MCP server as a subprocess using `uv run server.py`
3. `uv` automatically creates a virtual environment and installs dependencies on first run
4. The server advertises its available tools via the `tools/list` JSON-RPC method
5. During conversations, Claude can automatically call these tools when relevant
6. The server executes the requested tool and returns results to Claude
7. Claude incorporates the results into its response to you

## Development Approach

This project uses **PEP 723 inline dependency declarations** instead of a traditional project structure with `pyproject.toml` and lock files. This choice makes the server completely self-contained in a single file, which is ideal for:
- Learning and experimentation
- Easy sharing and portability
- Simple projects that don't need complex dependency management

For larger production projects, a traditional structure with `pyproject.toml`, lock files, and package structure would be more appropriate.