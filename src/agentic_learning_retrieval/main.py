from agentic_learning_retrieval.cli import main
from agentic_learning_retrieval.classification import classify_question
from agentic_learning_retrieval.models import QuestionFixture
from agentic_learning_retrieval.retrieval import (
    build_retrieval_query,
    decide_retrieval,
    retrieve_documents,
)

__all__ = [
    "QuestionFixture",
    "build_retrieval_query",
    "classify_question",
    "decide_retrieval",
    "main",
    "retrieve_documents",
]


if __name__ == "__main__":
    main()
