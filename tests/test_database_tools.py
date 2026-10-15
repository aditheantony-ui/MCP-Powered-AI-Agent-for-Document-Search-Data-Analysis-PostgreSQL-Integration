from server.tools.database_tools import query_database


def test_reject_delete():
    assert "SELECT" in query_database("DELETE FROM users")


def test_reject_multiple_statements():
    assert "Multiple statements" in query_database("SELECT 1; SELECT 2")
