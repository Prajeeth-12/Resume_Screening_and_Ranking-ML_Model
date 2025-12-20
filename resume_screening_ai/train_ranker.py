"""Wrapper to run the ML scoring trainer from the layered package."""
from layers.ml_scoring.train_ranker import train_ranker


if __name__ == "__main__":
    train_ranker()
