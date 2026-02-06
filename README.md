# session-audit-trails

Stores append-only JSONL session logs with event traces, handoffs, and startup/status artifacts for replay and debugging.

## Purpose
Create reliable, append-only session evidence for incident analysis, replayability, and governance review.

## Features
- Append-only JSONL event ledger (`session_memory.jsonl`).
- Standardized event types for escalations, tool actions, and outcomes.
- Session artifact capture (startup checks, handoffs, feature flags).
- Replay-oriented metadata for debugging and postmortems.
- Filterable trace export for external analysis.

## Config
- `AUDIT_LOG_PATH`: Path to append-only JSONL log.
- `AUDIT_INCLUDE_PAYLOADS`: Include or redact payload body fields.
- `AUDIT_FLUSH_INTERVAL_MS`: Buffer flush interval for event durability.
- `SESSION_ARTIFACT_DIR`: Directory for startup/handoff/status artifacts.
- `AUDIT_SCHEMA_VERSION`: Event schema version tag.

## Quickstart
```bash
mkdir -p .session_artifacts
export AUDIT_LOG_PATH=./session_memory.jsonl
python3 audit_runner.py --session-id demo-001
python3 replay.py --log ./session_memory.jsonl --session-id demo-001
```

## Usage
```bash
make setup
make check
make run
```

## Roadmap
- Add tamper-evident hash chaining for event streams.
- Add event compaction and archival rotation strategy.
- Add timeline visualizer for replay workflows.
- Add policy-linked audit assertions for CI.
