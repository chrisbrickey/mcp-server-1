# /// script
# dependencies = [
#     "mcp>=1.0.0"
# ]
# requires-python = ">=3.13"
# ///

"""
Simple MCP server providing time and date utilities.
Using inline dependency declaration at top of file in lieu of using pyproject.toml to manage dependencies.
"""

from datetime import datetime
from typing import Any

import anyio
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server


def get_current_date_impl() -> str:
    """
    Get the current date.

    Returns:
        Current date as a formatted string (YYYY-MM-DD)
    """
    today = datetime.now().date()
    return today.strftime("%Y-%m-%d")


def main() -> int:
    """Main entry point for the MCP server."""

    # Create server instance
    server = Server("time-date-server")

    # This annotation declares that this method will be called when MCP client (e.g. claude) requests list of tools.
    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        """List available tools."""
        return [
            types.Tool(
                name="get_current_date",
                description="Get the current date",
                inputSchema={
                    "type": "object",
                    "properties": {}
                }
            )
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
        result = get_current_date_impl()
        return [
            types.TextContent(
                type="text",
                text=result
            )
        ]

    async def arun():
        """Run the server with stdio transport."""
        async with stdio_server() as streams:
            await server.run(
                streams[0],
                streams[1],
                server.create_initialization_options()
            )

    anyio.run(arun)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
