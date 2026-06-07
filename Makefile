PYTHON ?= ./.venv/bin/python
LOCAL_ENV = env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src LANGSMITH_TRACING=false LANGCHAIN_TRACING_V2=false

.PHONY: help install sanity demo test

help:
	@printf "Available targets:\n"
	@printf "  make install              Install the project into the local venv without build isolation.\n"
	@printf "  make sanity               Run the Day 1 environment check.\n"
	@printf "  make demo                 Run the retrieval demo.\n"
	@printf "  make test                 Run deterministic tests.\n"

install:
	$(PYTHON) -m pip install -e . --no-build-isolation

sanity:
	$(LOCAL_ENV) $(PYTHON) -m agentic_learning_retrieval.main

demo:
	$(LOCAL_ENV) $(PYTHON) -m agentic_learning_retrieval.main

test:
	$(LOCAL_ENV) $(PYTHON) -m unittest discover -s tests -p 'test_*.py'
