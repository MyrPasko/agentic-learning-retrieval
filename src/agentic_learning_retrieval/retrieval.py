from __future__ import annotations

import re

from agentic_learning_retrieval.loaders import load_corpus_documents
from agentic_learning_retrieval.models import QuestionClassification

STOP_WORDS = frozenset(
    {"the", "and", "for", "with", "what", "does", "why", "who", "how"}
)


def decide_retrieval(classification: QuestionClassification) -> bool:
    return classification != "retrieval_not_needed"


def build_retrieval_query(question: str, should_retrieve: bool) -> str | None:
    if not should_retrieve:
        return None

    return question


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9-]+", text.lower())
    return [
        token
        for token in tokens
        if len(token) >= 3 and token not in STOP_WORDS
    ]


def retrieve_documents(query: str | None) -> list[str]:
    if query is None:
        return []

    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    matched_documents: list[str] = []

    for document in load_corpus_documents():
        document_text = document.content.lower()
        if any(token in document_text for token in query_tokens):
            matched_documents.append(document.content)

    return matched_documents
