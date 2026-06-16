from __future__ import annotations

import json

from agentic_learning_retrieval.models import CorpusDocument, QuestionFixture
from agentic_learning_retrieval.paths import get_corpus_path, get_questions_path


def load_questions() -> list[QuestionFixture]:
    questions_path = get_questions_path()

    with questions_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_corpus_documents() -> list[CorpusDocument]:
    corpus_path = get_corpus_path()
    sorted_files = sorted(
        [file for file in corpus_path.iterdir() if file.is_file()],
        key=lambda path: path.name,
    )

    return [
        CorpusDocument(
            source_id=document_path.stem,
            content=document_path.read_text(encoding="utf-8").strip(),
        )
        for document_path in sorted_files
    ]
