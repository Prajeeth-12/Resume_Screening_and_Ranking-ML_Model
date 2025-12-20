# Resume Screening AI

Minimal starter scaffold for an AI-based resume screening and candidate ranking system.

## Requirements
- Windows
- Python 3.10+
- Virtual environment recommended

## Quickstart (PowerShell)
```powershell
cd resume_screening_ai
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## Project Layout
- `app.py` — Streamlit entrypoint (PDF upload, extract, clean, display text)
- `requirements.txt` — pinned dependencies
- `data/` — sample resumes and job descriptions
- `utils/` — shared helpers (`resume_parser`, `text_cleaner`)
- `tests/` — lightweight pytest tests for utilities

## Notes
- Uses Streamlit for UI, spaCy for NLP, pdfplumber for PDF parsing, scikit-learn for TF-IDF and cosine similarity.
- No GPU or paid services required.

## Sample Data
- `data/sample_resume.pdf` — one-page text-based demo resume (Jane Doe, contact, skills Python/SQL, brief experience).

## How to run tests
```powershell
cd resume_screening_ai
python -m pytest
```
If `pytest` is not installed: `pip install pytest` inside the virtual environment.
