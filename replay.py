import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Replay audit events by session")
    parser.add_argument("--log", required=True)
    parser.add_argument("--session-id", required=True)
    args = parser.parse_args()

    log_path = Path(args.log)
    counts = Counter()
    total = 0

    for line in log_path.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("session_id") != args.session_id:
            continue
        total += 1
        counts[event.get("type", "unknown")] += 1

    summary = {"session_id": args.session_id, "total_events": total, "by_type": dict(counts)}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
