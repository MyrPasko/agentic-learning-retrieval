import unittest

from agentic_learning_retrieval.classification import classify_question
from agentic_learning_retrieval.models import QuestionFixture
from agentic_learning_retrieval.retrieval import (
    build_retrieval_query,
    decide_retrieval,
    retrieve_documents,
)


class RetrievalDemoTest(unittest.TestCase):
    def test_arithmetic_question_skips_retrieval(self) -> None:
        question: QuestionFixture = {
            "id": "q4",
            "question": "What is 12 multiplied by 8?",
            "expected_category": "retrieval_not_needed",
            "notes": "General reasoning; no corpus lookup needed.",
        }

        classification = classify_question(question)
        should_retrieve = decide_retrieval(classification)
        query = build_retrieval_query(question["question"], should_retrieve)
        results = retrieve_documents(query)

        self.assertEqual(classification, "retrieval_not_needed")
        self.assertFalse(should_retrieve)
        self.assertIsNone(query)
        self.assertEqual(results, [])

    def test_retrieval_needed_question_returns_corpus_matches(self) -> None:
        question: QuestionFixture = {
            "id": "q1",
            "question": "Who owns the Payments API?",
            "expected_category": "retrieval_needed",
            "notes": "Requires looking up a specific fact from the corpus.",
        }

        classification = classify_question(question)
        should_retrieve = decide_retrieval(classification)
        query = build_retrieval_query(question["question"], should_retrieve)
        results = retrieve_documents(query)

        self.assertEqual(classification, "retrieval_needed")
        self.assertTrue(should_retrieve)
        self.assertEqual(query, question["question"])
        self.assertTrue(results)
