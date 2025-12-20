"""Train a lightweight ranker on structured resume-JD features."""
from __future__ import annotations

from pathlib import Path
from typing import List

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("data/ranking_data.csv")
MODEL_PATH = Path.cwd() / "models" / "ranker.joblib"
FEATURE_COLUMNS: List[str] = [
    "skill_score",
    "exp_score",
    "edu_score",
    "semantic_score",
]


def _load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Ranking data not found at {path}")
    df = pd.read_csv(path)
    expected = set(FEATURE_COLUMNS + ["relevance_score", "resume_text", "jd_text"])
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in ranking data: {missing}")
    df = df.dropna(subset=FEATURE_COLUMNS + ["relevance_score"])
    if df.empty:
        raise ValueError("Ranking data is empty after dropping missing rows")
    return df


def train_ranker() -> None:
    df = _load_data(DATA_PATH)
    print("Loaded rows:", len(df))
    X = df[FEATURE_COLUMNS].to_numpy(dtype=float)
    y = df["relevance_score"].to_numpy(dtype=float)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Learned weights:", model.coef_)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("=== Ranker Evaluation ===")
    print(f"MSE: {mse:.4f}")
    print(f"R^2: {r2:.4f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "feature_order": FEATURE_COLUMNS}, MODEL_PATH)
    print(f"Saved ranker to {MODEL_PATH}")


if __name__ == "__main__":
    train_ranker()
