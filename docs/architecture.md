# Architecture

The project has four layers:

- `server/` exposes typed MCP tools through the official Python SDK.
- `document_processing/` provides local UTF-8 document loading and search.
- `database/` provides safe SQLite connections and read-only query execution.
- `agent/` builds grounded prompts and optionally calls an OpenAI-compatible model.

The MCP server runs over stdio by default, which makes it compatible with the VS Code MCP configuration in `.vscode/mcp.json`. Data processing uses standard-library modules so the server remains lightweight and easy to deploy.
