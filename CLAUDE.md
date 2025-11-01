# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

- **Python Version**: 3.13+
- **Package Manager**: uv (PEP 723 inline script metadata)
- **Framework**: Official MCP Python SDK (`mcp` package)
- **IDE**: PyCharm (configuration present in `.idea/`)

## Common Commands

### Running the Server
```bash
# Run the MCP server (dependencies are handled automatically by uv)
uv run server.py
```

On first run, `uv` will automatically:
- Create an isolated virtual environment
- Install the `mcp` package dependency
- Execute the server

### Modifying Dependencies
Dependencies are declared inline at the top of `server.py` using PEP 723 format:
```python
# /// script
# dependencies = [
#     "mcp>=1.0.0"
# ]
# requires-python = ">=3.13"
# ///
```

To add a new dependency, edit the `dependencies` list in the inline metadata block.

### Testing
```bash
# Testing framework to be configured
```