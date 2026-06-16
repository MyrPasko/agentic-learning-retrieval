# agentic-learning-retrieval

Project 3 of the agentic-learning track: a controlled retrieval workflow starter, not a generic "chat over docs" demo.

## Current Scope

The current local slice proves five explicit boundaries:

1. classify the question,
2. decide whether retrieval is needed,
3. generate a retrieval query,
4. retrieve grounded source candidates from a small corpus,
5. compare bootstrap classifications against fixture expectations.

The retrieval backend is intentionally simple. The point is to make the workflow boundary explicit before adding ranking, answer synthesis, query rewrite, or vector infrastructure.

## Project Structure

- `src/agentic_learning_retrieval/models.py` - shared typed data contracts
- `src/agentic_learning_retrieval/paths.py` - repo-local filesystem paths
- `src/agentic_learning_retrieval/loaders.py` - question and corpus loading
- `src/agentic_learning_retrieval/classification.py` - bootstrap question classification rules
- `src/agentic_learning_retrieval/retrieval.py` - retrieval decision, query building, tokenization, and lexical corpus matching
- `src/agentic_learning_retrieval/workflow.py` - bootstrap-to-retrieval workflow orchestration
- `src/agentic_learning_retrieval/cli.py` - command-line output surface
- `src/agentic_learning_retrieval/main.py` - thin compatibility entrypoint for `python -m`
- `data/corpus/` - small technical document corpus
- `data/questions/questions_v1.json` - first question fixtures
- `tests/` - deterministic checks for arithmetic skip and corpus-backed retrieval

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e . --no-build-isolation
```

## Commands

```bash
make sanity
make demo
make test
```

`make sanity`, `make demo`, and `make test` use `PYTHONPATH=src`, so the Day 1 slice can run even before an editable install succeeds.

## Current Output Contract

The runtime surface prints the workflow state for each fixture in order:

- question ids
- expected categories
- bootstrap classifications
- `match` / `mismatch`
- retrieval decisions
- retrieval queries
- retrieved document lists

That is enough for the bootstrap plus first corpus-backed retrieval slice. Ranking, source IDs, snippets, grounded answer synthesis, and evidence sufficiency belong to later days.
