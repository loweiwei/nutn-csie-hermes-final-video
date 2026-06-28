# Hermes + Linux Commands

These commands are provided for a real Hermes/Linux environment. The submitted project also includes deterministic mock/stub outputs so it can be completed without paid token or cloud API access.

## Basic local run

```bash
cd nutn_csie_hermes_final_project
python3 scripts/run_mock_workflow.py
python3 scripts/generate_video.py
```

## Optional Hermes transcript capture

If Hermes is available locally, you can capture raw agent outputs like this:

```bash
mkdir -p traces/raw_hermes

hermes chat --toolsets terminal --yolo -q "$(cat agents/planner_agent.md)

Input topic:
NUTN CSIE 60-second promotional video.
Please output JSON only." | tee traces/raw_hermes/01_planner_raw.md

hermes chat --toolsets terminal --yolo -q "$(cat agents/script_agent.md)

Input:
$(cat handoff/01_planner_output.json)
Please output JSON only." | tee traces/raw_hermes/02_script_raw.md

hermes chat --toolsets terminal --yolo -q "$(cat agents/visual_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
Please output JSON only." | tee traces/raw_hermes/03_visual_raw.md

hermes chat --toolsets terminal --yolo -q "$(cat agents/reviewer_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
$(cat handoff/03_visual_output.json)
Please output JSON only." | tee traces/raw_hermes/04_reviewer_raw.md

hermes chat --toolsets terminal --yolo -q "$(cat agents/finalizer_agent.md)

Input:
$(cat handoff/01_planner_output.json)
$(cat handoff/02_script_output.json)
$(cat handoff/03_visual_output.json)
$(cat handoff/04_reviewer_feedback.json)
Please output JSON only." | tee traces/raw_hermes/05_finalizer_raw.md
```

## Notes

- Do not upload API keys, token, passwords, or private screenshots.
- If Hermes output is unstable, keep the deterministic JSON files in `handoff/` as the final controlled handoff evidence.
- If you add real campus footage, update `outputs/asset_sources.md`.
