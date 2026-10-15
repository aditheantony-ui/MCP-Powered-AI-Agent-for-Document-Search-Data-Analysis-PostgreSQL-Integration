from pathlib import Path


def search_document(data_dir: Path, filename: str, keyword: str) -> str:
    """Search a text document for a keyword."""
    root = data_dir.resolve()
    path = (root / filename).resolve()
    if not path.is_relative_to(root):
        return "Error: Invalid file path."
    if path.suffix.lower() != ".txt":
        return "Error: Only .txt files are supported."
    if not path.is_file():
        return "Error: Document not found."
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        matches = [
            f"Line {index}: {line}"
            for index, line in enumerate(lines, 1)
            if keyword.casefold() in line.casefold()
        ]
        return "\n".join(matches) if matches else "No matches found."
    except OSError:
        return "Error: Unable to read document."
