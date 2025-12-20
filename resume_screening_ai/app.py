"""Resume screening demo with parsing, cleaning, and deterministic scoring."""
from pathlib import Path
from typing import List, Sequence

import streamlit as st

from utils.resume_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import SKILL_LIST, extract_skills, skill_match_score
from utils.matcher import compute_similarity


def main() -> None:
    st.title("Resume Screening AI")
    st.caption("Upload PDFs, compare against a job description, and rank candidates.")

    job_desc = st.text_area("Job Description", height=180, placeholder="Paste the target job description here...")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF resumes",
        type=["pdf"],
        accept_multiple_files=True,
        help="Multiple files supported for ranking",
    )

    if not uploaded_files:
        st.info("Please upload at least one PDF resume to continue.")
        return

    if not job_desc.strip():
        st.warning("Job description is empty. Add text to compute similarity scores.")

    results: List[dict] = []

    for index, uploaded_file in enumerate(uploaded_files, start=1):
        candidate_name = Path(uploaded_file.name).stem or f"Candidate {index}"

        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)

        matched_skills = extract_skills(cleaned_text)
        skill_pct = skill_match_score(matched_skills, len(SKILL_LIST))
        skill_norm = skill_pct / 100.0

        similarity = compute_similarity(job_desc, cleaned_text)

        final_score = 0.6 * similarity + 0.4 * skill_norm

        results.append(
            {
                "name": candidate_name,
                "matched_skills": matched_skills,
                "skill_pct": skill_pct,
                "similarity": similarity,
                "final_score": final_score,
                "cleaned_text": cleaned_text,
            }
        )

    ranked = sorted(results, key=lambda item: item["final_score"], reverse=True)

    st.subheader("Ranked Candidates")

    for entry in ranked:
        st.markdown(f"### {entry['name']}")

        matched_display = ", ".join(entry["matched_skills"]) if entry["matched_skills"] else "None"
        st.write(f"Matched skills: {matched_display}")
        st.write(f"Skill match %: {entry['skill_pct']:.1f}%")
        st.write(f"TF-IDF similarity: {entry['similarity']:.3f}")

        final_percent = entry["final_score"] * 100
        st.metric("Final score", f"{final_percent:.1f}%")
        st.caption("Ranked higher due to better skill match and higher semantic similarity")

        with st.expander("View cleaned text"):
            st.text_area("Cleaned Resume Text", value=entry["cleaned_text"], height=250)


if __name__ == "__main__":
    main()
