"""TF-IDF based resume-job description matcher."""
from __future__ import annotations

from typing import Iterable

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(job_desc: str, resume_text: str) -> float:
    """Return cosine similarity (0-1) between job description and resume text.

    Uses TF-IDF with English stop words; returns 0.0 if inputs are empty or the
    vectorizer cannot build a vocabulary.
    """
    if not job_desc or not resume_text:
        return 0.0

    documents: list[str] = [job_desc, resume_text]
    vectorizer = TfidfVectorizer(stop_words="english")
    try:
        matrix = vectorizer.fit_transform(documents)
        sim = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    except ValueError:
        # Happens when the vocabulary is empty after stop-word removal.
        return 0.0

    # Clamp to [0, 1] for safety.
    return max(0.0, min(1.0, float(sim)))
