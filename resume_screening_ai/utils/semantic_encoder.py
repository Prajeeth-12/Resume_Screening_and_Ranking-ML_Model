"""Semantic similarity utilities using Sentence-BERT bi-encoder."""
from __future__ import annotations

from typing import Optional

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_MODEL_NAME = "all-MiniLM-L6-v2"
_encoder: Optional[SentenceTransformer] = None


def _get_encoder() -> SentenceTransformer:
    global _encoder
    if _encoder is None:
        _encoder = SentenceTransformer(_MODEL_NAME, device="cpu")
    return _encoder


def get_semantic_similarity(resume_text: str, jd_text: str) -> float:
    """Return cosine similarity between resume and JD embeddings in [0, 1]."""
    if not resume_text or not jd_text:
        return 0.0

    encoder = _get_encoder()
    embeddings = encoder.encode([resume_text, jd_text], convert_to_numpy=True, normalize_embeddings=True)
    sim = float(cosine_similarity(embeddings[0:1], embeddings[1:2])[0][0])
    return max(0.0, min(1.0, sim))
