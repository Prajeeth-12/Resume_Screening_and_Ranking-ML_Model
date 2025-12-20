"""Skill normalization and synonym-aware matching."""
from __future__ import annotations

import re
from typing import Dict, Iterable, List, Set, Tuple


SYNONYM_MAP: Dict[str, List[str]] = {
    "react": ["react", "reactjs", "react.js", "react js"],
    "javascript": ["javascript", "js", "ecmascript", "java script"],
    "frontend": [
        "frontend",
        "front-end",
        "front end",
        "front-end developer",
        "front end developer",
        "frontend developer",
        "ui",
        "ui/ux",
    ],
    "typescript": ["typescript", "ts"],
    "html": ["html", "hypertext markup", "html5"],
    "css": ["css", "cascading style sheets", "css3"],
    "angular": ["angular", "angularjs", "angular.js"],
    "vue": ["vue", "vue.js", "nuxt"],
    "redux": ["redux"],
    "webpack": ["webpack"],
    "sass": ["sass", "scss"],
    "tailwind": ["tailwind"],
    "responsive design": ["responsive", "responsive design"],
    "cross browser": ["cross-browser", "cross browser"],
    "python": ["python"],
    "sql": ["sql"],
    "machine learning": ["machine learning", "ml"],
    "pandas": ["pandas"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "api": ["api", "rest", "restful"],
    "cloud": ["cloud", "aws", "azure", "gcp"],
    "cicd": ["cicd", "ci/cd", "continuous integration", "continuous delivery"],
    "statistics": ["statistics", "statistical"],
    "deep learning": ["deep learning", "dl"],
    "nlp": ["nlp", "natural language processing"],
    "testing": ["testing", "qa", "quality assurance"],
    "automation": ["automation", "test automation"],
}

_PATTERN_CACHE: Dict[str, List[re.Pattern[str]]] = {}


def _get_patterns() -> Dict[str, List[re.Pattern[str]]]:
    if _PATTERN_CACHE:
        return _PATTERN_CACHE
    for canonical, synonyms in SYNONYM_MAP.items():
        _PATTERN_CACHE[canonical] = [
            re.compile(rf"\b{re.escape(term)}\b", flags=re.IGNORECASE) for term in synonyms
        ]
    return _PATTERN_CACHE


def extract_normalized_skills(text: str) -> Set[str]:
    if not text:
        return set()
    patterns = _get_patterns()
    normalized: Set[str] = set()
    for canonical, regexes in patterns.items():
        if any(rx.search(text) for rx in regexes):
            normalized.add(canonical)
    return normalized


def score_skill_matches(
    resume_text: str,
    required_skills: Iterable[str],
    optional_skills: Iterable[str],
) -> Dict[str, object]:
    normalized_resume = extract_normalized_skills(resume_text.lower())
    req_set = {s.lower() for s in required_skills}
    opt_set = {s.lower() for s in optional_skills}

    matched_required = sorted(normalized_resume & req_set)
    missing_required = sorted(req_set - normalized_resume)
    matched_optional = sorted(normalized_resume & opt_set)

    skill_score = (len(matched_required) / len(req_set)) if req_set else 0.0
    bonus = 0.1 * (len(matched_optional) / len(opt_set)) if opt_set else 0.0
    skill_score = min(1.0, skill_score + bonus)

    return {
        "skill_score": skill_score,
        "matched_required": matched_required,
        "missing_required": missing_required,
        "matched_optional": matched_optional,
    }
