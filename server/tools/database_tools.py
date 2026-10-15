import re

from database.connection import get_connection


def query_database(sql: str) -> str:
    """Execute a restricted read-only SQL query."""
    statement = sql.strip().rstrip(";").strip()
    if not statement:
        return "Error: Query cannot be empty."
    if ";" in statement:
        return "Error: Multiple statements are not allowed."
    if not re.match(r"(?is)^SELECT\b", statement):
        return "Error: Only SELECT queries are permitted."
    if re.search(
        r"(?i)\b(insert|update|delete|drop|alter|create|truncate|"
        r"grant|revoke|copy|call|execute|merge|into|pg_sleep)\b",
        statement,
    ):
        return "Error: Prohibited SQL operation."
    try:
        with get_connection() as connection:
            connection.execute("SET TRANSACTION READ ONLY")
            connection.execute("SET LOCAL statement_timeout = '3000ms'")
            with connection.cursor() as cursor:
                cursor.execute(statement)
                if cursor.description is None:
                    return "No results returned."
                columns = [column.name for column in cursor.description]
                rows = cursor.fetchall()
                return "\n".join(
                    [", ".join(columns)]
                    + [", ".join(str(value) for value in row) for row in rows]
                ) or "No results returned."
    except Exception as exc:
        return f"Error: Database query failed ({type(exc).__name__})."
