from __future__ import annotations

from pathlib import Path


def get_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_questions_path() -> Path:
    return get_repo_root() / "data" / "questions" / "questions_v1.json"


def get_corpus_path() -> Path:
    return get_repo_root() / "data" / "corpus"
