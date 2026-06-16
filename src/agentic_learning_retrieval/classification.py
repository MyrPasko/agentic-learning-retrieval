from __future__ import annotations

from agentic_learning_retrieval.models import QuestionClassification, QuestionFixture


def classify_question(question_fixture: QuestionFixture) -> QuestionClassification:
    question = question_fixture["question"].lower()

    if "multiplied" in question:
        return "retrieval_not_needed"
    if "why" in question or "explain" in question:
        return "ambiguous"
    return "retrieval_needed"


def compare_classifications(
    expected: list[str],
    actual: list[QuestionClassification],
) -> list[str]:
    return [
        "match" if expected_item == actual_item else "mismatch"
        for expected_item, actual_item in zip(expected, actual)
    ]
