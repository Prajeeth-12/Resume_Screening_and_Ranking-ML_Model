"""Deterministic skill extraction utilities."""
from __future__ import annotations

import re
from typing import Iterable, List

# Expand this list as needed; keep lowercase for normalized matching.
SKILL_LIST: List[str] = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "scikit learn",
    "machine learning",
    "data analysis",
    "airflow",
    "spark",
    "docker",
    "kubernetes",
    "tableau",
    "power bi",
]


def _build_pattern(skill: str) -> re.Pattern[str]:
    return re.compile(rf"\b{re.escape(skill)}\b", flags=re.IGNORECASE)


def extract_skills(cleaned_text: str) -> list[str]:
    """Return unique matched skills using word-boundary regexes."""
    if not cleaned_text:
        return []

    matches: list[str] = []
    for skill in SKILL_LIST:
        if _build_pattern(skill).search(cleaned_text):
            matches.append(skill)

    return sorted(set(matches))


def skill_match_score(matched_skills: Iterable[str], total_required: int) -> float:
    """Compute percentage score based on matched vs required skills."""
    if total_required <= 0:
        return 0.0

    matched_count = len(set(matched_skills))
    return (matched_count / total_required) * 100.0
