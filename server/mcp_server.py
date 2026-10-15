from pathlib import Path

from mcp.server.fastmcp import FastMCP

from server.tools.data_tools import analyze_file
from server.tools.database_tools import query_database
from server.tools.document_tools import search_document

mcp = FastMCP("MCP-Powered-AI-Agent")
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@mcp.tool()
def document_search(filename: str, keyword: str) -> str:
    """Search a text document for a keyword."""
    return search_document(DATA_DIR, filename, keyword)


@mcp.tool()
def analyze_csv_excel(filename: str) -> str:
    """Analyze a CSV or Excel file."""
    return analyze_file(DATA_DIR, filename)


@mcp.tool()
def postgres_read_query(sql: str) -> str:
    """Run a restricted read-only PostgreSQL SELECT query."""
    return query_database(sql)


if __name__ == "__main__":
    mcp.run(transport="stdio")
