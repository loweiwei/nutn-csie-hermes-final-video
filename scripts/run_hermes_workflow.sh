#!/usr/bin/env bash
set -euo pipefail

mkdir -p traces/raw_hermes

echo "[Hermes optional run] Planner Agent"
hermes chat --toolsets terminal --yolo -q "$(cat agents/planner_agent.md)

Input topic:
NUTN CSIE 60-second promotional video.
Please output JSON only." | tee traces/raw_hermes/01_planner_raw.md

echo "[Hermes optional run] Script Agent"
hermes chat --toolsets terminal --yolo -q "$(cat agents/script_agent.md)

Input:
$(cat handoff/01_planner_output.json)
Please output JSON only." | tee traces/raw_hermes/02_script_raw.md

echo "[Hermes optional run] Visual Agent"
hermes chat --toolsets terminal --yolo -q "$(cat agents/visual_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
Please output JSON only." | tee traces/raw_hermes/03_visual_raw.md

echo "[Hermes optional run] Reviewer Agent"
hermes chat --toolsets terminal --yolo -q "$(cat agents/reviewer_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
$(cat handoff/03_visual_output.json)
Please output JSON only." | tee traces/raw_hermes/04_reviewer_raw.md

echo "[Hermes optional run] Finalizer Agent"
hermes chat --toolsets terminal --yolo -q "$(cat agents/finalizer_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
$(cat handoff/03_visual_output.json)
$(cat handoff/04_reviewer_feedback.json)
Please output JSON only." | tee traces/raw_hermes/05_finalizer_raw.md
