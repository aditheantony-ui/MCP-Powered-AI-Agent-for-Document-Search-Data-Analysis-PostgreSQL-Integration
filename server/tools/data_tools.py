from pathlib import Path
import pandas as pd


def analyze_file(data_dir: Path, filename: str) -> str:
    """Analyze a CSV or Excel file."""
    root = data_dir.resolve()
    path = (root / filename).resolve()
    if not path.is_relative_to(root):
        return "Error: Invalid file path."
    if path.suffix.lower() not in {".csv", ".xlsx", ".xls"}:
        return "Error: Unsupported file format."
    if not path.is_file():
        return "Error: File not found."
    try:
        frame = pd.read_csv(path) if path.suffix.lower() == ".csv" else pd.read_excel(path)
        if frame.empty:
            return "The file contains no data rows."
        return (
            f"File: {path.name}\n"
            f"Rows: {len(frame)}\n"
            f"Columns: {len(frame.columns)}\n"
            f"Column names: {', '.join(map(str, frame.columns))}\n\n"
            f"Preview:\n{frame.head().to_string(index=False)}\n\n"
            f"Statistics:\n{frame.describe(include='all').to_string()}"
        )
    except (OSError, ValueError) as exc:
        return f"Error: Unable to analyze file ({type(exc).__name__})."
