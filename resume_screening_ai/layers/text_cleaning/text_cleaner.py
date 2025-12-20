"""Utilities for cleaning extracted resume text."""
import re
from typing import Optional


_CLEAN_PATTERN = re.compile(r"[^a-zA-Z\s]+")
_SPACE_PATTERN = re.compile(r"\s+")


def clean_text(text: Optional[str]) -> str:
    """Normalize resume text by lowercasing and removing non-letters."""
    if not text:
        return ""

    lowered = text.lower()
    letters_only = _CLEAN_PATTERN.sub(" ", lowered)
    squashed = _SPACE_PATTERN.sub(" ", letters_only)
    return squashed.strip()
