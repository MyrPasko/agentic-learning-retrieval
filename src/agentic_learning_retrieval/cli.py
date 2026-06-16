from __future__ import annotations

from agentic_learning_retrieval.workflow import run_retrieval_workflow


def main() -> None:
    workflow_snapshot = run_retrieval_workflow()

    print(f"Loaded {len(workflow_snapshot.question_ids)} questions")
    print("\n".join(workflow_snapshot.question_ids))
    print("\n".join(workflow_snapshot.expected_categories))
    print("\n".join(workflow_snapshot.bootstrap_classifications))
    print("\n".join(workflow_snapshot.comparison))
    print("\n".join(map(str, workflow_snapshot.retrieval_decisions)))
    print("\n".join(map(str, workflow_snapshot.retrieval_queries)))
    print("\n".join(map(str, workflow_snapshot.retrieved_documents)))
