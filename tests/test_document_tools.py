from server.tools.document_tools import search_document


def test_search_document(tmp_path):
    (tmp_path / "sample.txt").write_text(
        "MCP server works\nCSV analysis", encoding="utf-8"
    )
    result = search_document(tmp_path, "sample.txt", "MCP")
    assert "MCP server works" in result


def test_missing_document(tmp_path):
    result = search_document(tmp_path, "missing.txt", "MCP")
    assert "not found" in result.lower()
