"""Document loading primitives shared by the MCP tools."""

from pathlib import Path


def load_document(path: Path) -> str:
    """Load a UTF-8 document and fail clearly for missing paths."""
    if not path.is_file():
        raise FileNotFoundError(f"Document not found: {path}")
    return path.read_text(encoding="utf-8")


def search_document(path: Path, query: str) -> list[str]:
    """Find non-empty lines containing query, case-insensitively."""
    if not query.strip():
        raise ValueError("query must not be empty")
    needle = query.casefold()
    return [line for line in load_document(path).splitlines() if needle in line.casefold()]
