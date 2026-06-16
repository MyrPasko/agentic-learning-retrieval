from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypedDict

QuestionClassification = Literal[
    "retrieval_not_needed", "ambiguous", "retrieval_needed"
]


class QuestionFixture(TypedDict):
    id: str
    question: str
    expected_category: str
    notes: str


@dataclass(frozen=True, slots=True)
class CorpusDocument:
    source_id: str
    content: str
