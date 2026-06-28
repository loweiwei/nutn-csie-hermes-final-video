#!/usr/bin/env python3
from pathlib import Path
import json

base = Path(__file__).resolve().parents[1]
required = [
    "handoff/01_planner_output.json",
    "handoff/02_script_output.json",
    "handoff/03_visual_output.json",
    "handoff/04_reviewer_feedback.json",
    "handoff/05_finalizer_output.json",
]
print("[mock workflow] checking deterministic agent handoff files...")
for item in required:
    path = base / item
    if not path.exists():
        raise FileNotFoundError(item)
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"[ok] {item}: {data.get('project_title', 'no title')}")
print("[done] zero-paid-token mock/stub workflow is reproducible.")
