import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def emit(path: Path, event: dict) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Append-only audit runner")
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--log", default=None)
    args = parser.parse_args()

    log_path = Path(args.log or "session_memory.jsonl")
    now = datetime.now(timezone.utc).isoformat()

    emit(log_path, {"type": "startup_checklist", "session_id": args.session_id, "timestamp": now, "status": "ok"})
    emit(log_path, {"type": "action_outcome", "session_id": args.session_id, "timestamp": now, "action": "demo_action", "result": "success"})
    emit(log_path, {"type": "handoff", "session_id": args.session_id, "timestamp": now, "next": "operator_review"})

    print(f"Wrote events to {log_path}")


if __name__ == "__main__":
    main()
