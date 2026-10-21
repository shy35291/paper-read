
from pathlib import Path
import pymupdf


def read_text(filename):
    """Read a TXT file."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def read_pdf(filename):
    """Extract text from a PDF file."""
    filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if filename.suffix.lower() != ".pdf":
        raise ValueError(f"Not a PDF file: {filename}")

    text_parts = []

    with pymupdf.open(filename) as pdf:
        for page in pdf:
            text_parts.append(page.get_text())

    return "\n".join(text_parts)
