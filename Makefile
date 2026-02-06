PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: setup check run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check:
	rm -f session_memory.jsonl
	$(PY) audit_runner.py --session-id make-check
	$(PY) replay.py --log ./session_memory.jsonl --session-id make-check

run:
	$(PY) audit_runner.py --session-id run-demo
