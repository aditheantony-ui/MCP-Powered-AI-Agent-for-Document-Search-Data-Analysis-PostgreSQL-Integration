
import sys
from pathlib import Path

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from server.tools.data_tools import analyze_file
from server.tools.document_tools import search_document

DATA_DIR = PROJECT_ROOT / "data"


def main():
    print("=== MCP-Powered AI Agent Demo ===\n")

    print("1. CSV Analysis")
    print(analyze_file(DATA_DIR, "sample.csv"))

    print("\n2. Document Search")
    print(search_document(DATA_DIR, "sample_document.txt", "AI"))


if __name__ == "__main__":
    main()
