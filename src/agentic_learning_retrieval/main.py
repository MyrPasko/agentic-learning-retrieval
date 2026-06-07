import json
import re
from typing import Literal, TypedDict

from agentic_learning_retrieval.helpers.path_helpers import (
    get_corpuses_path,
    get_questions_path,
)

STOP_WORDS = ["the", "and", "for", "with", "what", "does", "why", "who", "how"]

QuestionClassification = Literal[
    "retrieval_not_needed", "ambiguous", "retrieval_needed"
]


class QuestionFixture(TypedDict):
    id: str
    question: str
    expected_category: str
    notes: str


def classify_question(question_object: QuestionFixture) -> QuestionClassification:
    question = question_object["question"].lower()
    if "multiplied" in question:
        return "retrieval_not_needed"
    elif "why" in question or "explain" in question:
        return "ambiguous"
    else:
        return "retrieval_needed"


def get_bootstrap_classifications(questions: list[QuestionFixture]) -> list[str]:
    return [classify_question(question) for question in questions]


def compare_classifications(expected: list[str], actual: list[str]) -> list[str]:
    return [
        "match" if expected_item == actual_item else "mismatch"
        for expected_item, actual_item in zip(expected, actual)
    ]


def decide_retrieval(classification: QuestionClassification) -> bool:
    return classification != "retrieval_not_needed"


def get_retrieval_decisions(questions: list[QuestionFixture]) -> list[bool]:
    return [decide_retrieval(classify_question(question)) for question in questions]


def get_questions() -> list[QuestionFixture]:
    questions_path = get_questions_path()

    with open(questions_path, "r") as file:
        questions_input = json.load(file)

    return questions_input


def get_corpus_documents() -> list[str]:
    texts = []
    corpuses_path = get_corpuses_path()
    sorted_files = sorted(
        [file for file in corpuses_path.iterdir() if file.is_file()],
        key=lambda x: x.name,
    )

    for child in sorted_files:
        content = child.read_text(encoding="utf-8").strip()
        texts.append(content)

    return texts


def get_categories(questions: list[QuestionFixture]) -> list[str]:
    return [question["expected_category"] for question in questions]


def get_question_ids(questions: list[QuestionFixture]) -> list[str]:
    return [question["id"] for question in questions]


def build_retrieval_query(question: str, should_retrieve: bool) -> str | None:
    if should_retrieve:
        return question
    else:
        return None


def get_retrieval_queries(questions: list[QuestionFixture]) -> list[str | None]:
    return [
        build_retrieval_query(
            question["question"], decide_retrieval(classify_question(question))
        )
        for question in questions
    ]


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[a-z0-9-]+", text.lower())
    return [token for token in tokens if len(token) >= 3 and token not in STOP_WORDS]


def retrieve_documents(query: str | None) -> list[str]:
    if query is None:
        return []

    tokenized_query = tokenize(query)
    results = []

    if len(tokenized_query) == 0:
        return []
    else:
        retrieved_documents = get_corpus_documents()

        for document in retrieved_documents:
            if any(word in document.lower() for word in tokenized_query):
                results.append(document)
            else:
                continue

        return results


def get_retrieved_documents(queries: list[str | None]) -> list[list[str]]:
    return [retrieve_documents(query) for query in queries]


def main():
    result = get_questions()
    result_ids = get_question_ids(result)
    results_categories = get_categories(result)
    bootstrap_classifications = get_bootstrap_classifications(result)
    comparison = compare_classifications(results_categories, bootstrap_classifications)
    retrieve_decisions = get_retrieval_decisions(result)
    retrieval_queries = get_retrieval_queries(result)
    retrieved_documents = get_retrieved_documents(retrieval_queries)
    print(f"Loaded {len(result)} questions")
    print("\n".join(result_ids))
    print("\n".join(results_categories))
    print("\n".join(bootstrap_classifications))
    print("\n".join(map(str, comparison)))
    print("\n".join(map(str, retrieve_decisions)))
    print("\n".join(map(str, retrieval_queries)))
    print("\n".join(map(str, retrieved_documents)))


if __name__ == "__main__":
    main()
