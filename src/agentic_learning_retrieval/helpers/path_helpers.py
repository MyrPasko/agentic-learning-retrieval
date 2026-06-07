from pathlib import Path


def get_questions_path():
    return Path(__file__).resolve().parents[3] / "data/questions/questions_v1.json"


def get_corpuses_path():
    return Path(__file__).resolve().parents[3] / "data/corpus"
