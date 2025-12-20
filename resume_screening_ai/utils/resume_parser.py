"""Utilities for extracting raw text from PDF resumes."""
from typing import Any

import pdfplumber


def extract_text_from_pdf(file: Any) -> str:
    """Extract text from a PDF file-like object safely.

    Handles empty pages by skipping them. Returns a single string with page
    breaks preserved as blank lines.
    """
    if file is None:
        return ""

    try:
        file.seek(0)  # ensure beginning of file
    except Exception:
        pass

    text_chunks: list[str] = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            page_text = page_text.strip()
            if page_text:
                text_chunks.append(page_text)

    return "\n\n".join(text_chunks).strip()
