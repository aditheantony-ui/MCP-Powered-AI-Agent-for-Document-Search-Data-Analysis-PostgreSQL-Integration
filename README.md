# MCP Powered AI Agent

A Python 3.11+ Model Context Protocol server for local documents, CSV data, and read-only SQLite queries. It also includes a small optional LLM workflow and placeholders for fine-tuning/evaluation experiments.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
python main.py
```

The server communicates over stdio. VS Code can launch it using `.vscode/mcp.json`; open the project in VS Code and use the MCP tools from an MCP-enabled chat session.

Run the local demo with:

```powershell
python scripts/demo.py
```

To enable the optional document-question workflow, install `openai` and set `OPENAI_API_KEY` using `.env.example` as a template.

## Tools

- `read_document(path)` reads a UTF-8 text document.
- `search_document_text(path, query)` finds matching lines.
- `inspect_csv(path, preview_rows)` returns columns and a bounded preview.
- `query_database(database_path, query)` runs `SELECT`, `WITH`, or `PRAGMA` queries only.

## Docker

```powershell
docker compose -f deployment/docker-compose.yml up --build
```
