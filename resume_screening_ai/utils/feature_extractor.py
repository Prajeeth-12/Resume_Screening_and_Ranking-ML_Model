"""Feature extraction for ranking (skills, experience, education, semantics)."""
from __future__ import annotations

import re
from typing import Dict, Iterable, Optional

from utils.semantic_encoder import get_semantic_similarity
from utils.text_cleaner import clean_text
from utils.skill_normalizer import score_skill_matches


_DEGREE_KEYWORDS = {"bachelor", "master", "phd", "b.sc", "m.sc", "btech", "mtech", "mba"}


def _years_in_text(text: str) -> int:
    matches = re.findall(r"(\d+)\s+year", text.lower())
    years = [int(m) for m in matches]
    return max(years) if years else 0


def _education_score(resume_text: str, jd_text: str) -> float:
    resume_tokens = set(t for t in _DEGREE_KEYWORDS if t in resume_text.lower())
    jd_tokens = set(t for t in _DEGREE_KEYWORDS if t in jd_text.lower())
    if not jd_tokens:
        return 1.0 if resume_tokens else 0.0
    intersection = resume_tokens & jd_tokens
    return len(intersection) / len(jd_tokens)


def _experience_score(resume_text: str, jd_text: str, min_experience: Optional[int]) -> float:
    resume_years = _years_in_text(resume_text)
    jd_years = min_experience if min_experience is not None else _years_in_text(jd_text)
    if jd_years == 0:
        return 1.0 if resume_years > 0 else 0.0
    return min(resume_years / jd_years, 1.0)


def _education_score_preference(resume_text: str, education_preference: Optional[str]) -> float:
    if not education_preference:
        return 1.0
    education_preference = education_preference.lower()
    resume_tokens = resume_text.lower()
    return 1.0 if education_preference in resume_tokens else 0.0


def extract_features(
    resume_text: str,
    jd_text: str,
    required_skills: Optional[Iterable[str]] = None,
    optional_skills: Optional[Iterable[str]] = None,
    min_experience: Optional[int] = None,
    education_preference: Optional[str] = None,
    skill_match: Optional[Dict[str, object]] = None,
) -> Dict[str, float]:
    """Return normalized feature dict for ranking.

    Features:
    - skill_match_score: fraction of predefined skills matched
    - experience_score: ratio of resume years to JD-required years (clipped 0-1)
    - education_match_score: degree keyword overlap ratio
    - semantic_similarity: Sentence-BERT cosine similarity
    """
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    if required_skills is not None:
        match = skill_match or score_skill_matches(resume_text, required_skills, optional_skills or [])
        skill_score = float(match.get("skill_score", 0.0))
    else:
        match = None
        skill_score = 0.0

    exp_score = _experience_score(resume_text, jd_text, min_experience)
    if education_preference:
        edu_score = _education_score_preference(resume_text, education_preference)
    else:
        edu_score = _education_score(resume_text, jd_text)
    semantic_score = get_semantic_similarity(resume_text, jd_text)

    return {
        "skill_score": skill_score,
        "exp_score": exp_score,
        "edu_score": edu_score,
        "semantic_score": semantic_score,
    }
