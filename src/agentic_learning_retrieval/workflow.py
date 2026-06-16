from __future__ import annotations

from dataclasses import dataclass

from agentic_learning_retrieval.classification import (
    classify_question,
    compare_classifications,
)
from agentic_learning_retrieval.loaders import load_questions
from agentic_learning_retrieval.models import QuestionClassification
from agentic_learning_retrieval.retrieval import (
    build_retrieval_query,
    decide_retrieval,
    retrieve_documents,
)


@dataclass(frozen=True, slots=True)
class WorkflowSnapshot:
    question_ids: list[str]
    expected_categories: list[str]
    bootstrap_classifications: list[QuestionClassification]
    comparison: list[str]
    retrieval_decisions: list[bool]
    retrieval_queries: list[str | None]
    retrieved_documents: list[list[str]]


def run_retrieval_workflow() -> WorkflowSnapshot:
    questions = load_questions()
    question_ids = [question["id"] for question in questions]
    expected_categories = [question["expected_category"] for question in questions]
    bootstrap_classifications = [
        classify_question(question) for question in questions
    ]
    retrieval_decisions = [
        decide_retrieval(classification)
        for classification in bootstrap_classifications
    ]
    retrieval_queries = [
        build_retrieval_query(question["question"], should_retrieve)
        for question, should_retrieve in zip(questions, retrieval_decisions)
    ]
    retrieved_documents = [
        retrieve_documents(query) for query in retrieval_queries
    ]

    return WorkflowSnapshot(
        question_ids=question_ids,
        expected_categories=expected_categories,
        bootstrap_classifications=bootstrap_classifications,
        comparison=compare_classifications(
            expected_categories,
            bootstrap_classifications,
        ),
        retrieval_decisions=retrieval_decisions,
        retrieval_queries=retrieval_queries,
        retrieved_documents=retrieved_documents,
    )
