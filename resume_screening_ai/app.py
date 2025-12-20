"""Resume screening demo with parsing, cleaning, and learned/fallback ranking."""
from pathlib import Path
from typing import List, Sequence, Optional, Tuple

import joblib
import streamlit as st

from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.matcher import compute_similarity
from utils.feature_extractor import extract_features
from utils.jd_builder import JOB_ROLE_CONFIG, ROLE_CATEGORIES, build_jd
from utils.skill_normalizer import score_skill_matches


RANKER_PATH = Path("models/ranker.joblib")


@st.cache_resource(show_spinner=False)
def _load_ranker() -> Optional[Tuple[object, List[str]]]:
    if not RANKER_PATH.exists():
        return None
    artifact = joblib.load(RANKER_PATH)
    model = artifact.get("model")
    feature_order = artifact.get("feature_order")
    if model is None or feature_order is None:
        return None
    return model, feature_order


def main() -> None:
    st.title("Resume Screening AI")
    st.caption("Upload PDFs, compare against a job description, and rank candidates.")

    ranker_artifact = _load_ranker()

    st.subheader("Job setup")
    categories = sorted(ROLE_CATEGORIES.keys())
    selected_category = st.selectbox(
        "Select job family",
        options=categories,
        index=0,
        help="Pick a broader job family first",
    )
    available_roles = sorted(ROLE_CATEGORIES.get(selected_category, JOB_ROLE_CONFIG.keys()))
    job_title = st.selectbox(
        "Select job title",
        options=available_roles,
        index=0,
        help="Type to search and pick a role within the family",
    )
    experience_years = st.slider("Target experience (years)", min_value=0, max_value=15, value=3)

    canonical_jd = build_jd(job_title, experience_years)
    job_desc = canonical_jd["description"]

    st.caption("Using generated job description from selected role and experience.")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF resumes",
        type=["pdf"],
        accept_multiple_files=True,
        help="Multiple files supported for ranking",
    )

    if not uploaded_files:
        st.info("Please upload at least one PDF resume to continue.")
        return

    results: List[dict] = []

    for index, uploaded_file in enumerate(uploaded_files, start=1):
        candidate_name = Path(uploaded_file.name).stem or f"Candidate {index}"

        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)

        # Synonym-aware skills
        skill_match = score_skill_matches(
            resume_text=raw_text,
            required_skills=canonical_jd["required_skills"],
            optional_skills=canonical_jd["optional_skills"],
        )

        matched_skills = skill_match["matched_required"]
        missing_skills = skill_match["missing_required"]
        optional_matched = skill_match["matched_optional"]
        skill_norm = float(skill_match["skill_score"])
        skill_pct = skill_norm * 100

        similarity = compute_similarity(job_desc, cleaned_text)

        features = extract_features(
            raw_text,
            job_desc,
            required_skills=canonical_jd["required_skills"],
            optional_skills=canonical_jd["optional_skills"],
            min_experience=canonical_jd["min_experience"],
            education_preference=canonical_jd["education_preference"],
            skill_match=skill_match,
        )

        used_ranker = False
        if ranker_artifact is not None:
            model, feature_order = ranker_artifact
            vector = [features.get(name, 0.0) for name in feature_order]
            try:
                final_score = float(model.predict([vector])[0])
                used_ranker = True
            except Exception:
                final_score = 0.6 * similarity + 0.4 * skill_norm
        else:
            final_score = 0.6 * similarity + 0.4 * skill_norm

        results.append(
            {
                "name": candidate_name,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "matched_optional": optional_matched,
                "skill_pct": skill_pct,
                "similarity": similarity,
                "final_score": final_score,
                "features": features,
                "used_ranker": used_ranker,
                "cleaned_text": cleaned_text,
            }
        )

    ranked = sorted(results, key=lambda item: item["final_score"], reverse=True)

    st.subheader("Ranked Candidates")

    for entry in ranked:
        st.markdown(f"### {entry['name']}")

        st.write(f"Skill match %: {entry['skill_pct']:.1f}%")
        st.write(f"TF-IDF similarity: {entry['similarity']:.3f}")

        features = entry.get("features", {})
        st.write(
            f"Feature scores — Skills: {features.get('skill_score', 0.0):.2f}, "
            f"Experience: {features.get('exp_score', 0.0):.2f}, "
            f"Education: {features.get('edu_score', 0.0):.2f}, "
            f"Semantic: {features.get('semantic_score', 0.0):.2f}"
        )

        if entry.get("used_ranker"):
            st.metric("Final score (ML ranker)", f"{entry['final_score']:.2f}")
            st.caption("Ranked higher due to learned weighting of semantic similarity, skills, experience, and education signals.")
        else:
            final_percent = entry["final_score"] * 100
            st.metric("Final score", f"{final_percent:.1f}%")
            st.caption("Ranked by fallback TF-IDF similarity + skill coverage blend.")

        with st.expander("View cleaned text"):
            st.text_area("Cleaned Resume Text", value=entry["cleaned_text"], height=250)


if __name__ == "__main__":
    main()
