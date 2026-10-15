from server.mcp_server import mcp


def test_server_registers_expected_tools() -> None:
    tool_names = {tool.name for tool in mcp._tool_manager.list_tools()}
    assert tool_names == {
        "document_search",
        "analyze_csv_excel",
        "postgres_read_query",
    }
