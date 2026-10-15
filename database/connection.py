import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Connect to PostgreSQL using environment variables."""
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise RuntimeError("DB_PASSWORD is not configured.")
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "mcp_agent"),
        user=os.getenv("DB_USER", "mcp_readonly"),
        password=password,
        connect_timeout=5,
    )
