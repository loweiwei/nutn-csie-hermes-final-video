# 國立臺南大學資訊工程學系 60 秒形象宣傳影片

本專案使用 **Hermes Agent + Linux** 的零付費 token 路徑，設計一個可追蹤、可控制、可重現的多代理人短影片製作 workflow，最後輸出一支符合 55 至 65 秒規範的短影片。正式提交影片為學生自行剪輯版本；Python/PIL 生成版本保留作為無法實拍或重新製作時的備案。

- Project: NUTN CSIE 60-second promotional video
- Team member: 羅暐媁
- Platform: Hermes Agent on Linux
- Video: `outputs/final_video.mp4`
- Final video spec: 64.5 seconds, 1920x1080 MP4, H.264 video with AAC audio
- Report: `report/Final_Report_NUTN_CSIE_Hermes.pdf`
- Run mode: zero-paid-token mock/stub workflow, with deterministic handoff files and self-shot production plan
- Bonus theme: NUTN CSIE 60-second promotional video

## Repository guide

```text
.
├── README.md
├── report/
│   ├── Final_Report_NUTN_CSIE_Hermes.pdf
│   └── Final_Report_NUTN_CSIE_Hermes.md
├── agents/
│   ├── planner_agent.md
│   ├── script_agent.md
│   ├── visual_agent.md
│   ├── reviewer_agent.md
│   └── finalizer_agent.md
├── handoff/
│   ├── 01_planner_output.json
│   ├── 02_script_output.json
│   ├── 03_visual_output.json
│   ├── 04_reviewer_feedback.json
│   └── 05_finalizer_output.json
├── traces/
│   ├── execution_trace.md
│   └── hermes_linux_commands.md
├── outputs/
│   ├── final_video.mp4
│   ├── subtitles.srt
│   ├── asset_sources.md
│   └── video_storyboard.md
├── baseline/
│   └── single_agent_baseline.md
└── scripts/
    ├── generate_video.py
    ├── run_mock_workflow.py
    └── run_hermes_workflow.sh
```

## How to read this project

1. Read `report/Final_Report_NUTN_CSIE_Hermes.pdf` for the complete explanation.
2. Check `agents/` for each specialized agent role, prompt, input/output format, and tool policy.
3. Check `handoff/` for structured JSON handoff outputs.
4. Check `traces/execution_trace.md` for the zero-paid-token dry-run trace.
5. Check `outputs/video_storyboard.md` for the detailed self-shot scene plan.
6. Watch `outputs/final_video.mp4`.
7. Check `outputs/asset_sources.md` for copyright, source, consent, and safety notes.
8. Check `baseline/single_agent_baseline.md` for the single-agent baseline comparison.

## Zero-paid-token declaration

This project can be completed without paid LLM API, commercial AI video tools, personal API keys, or paid token quota.  
The submitted workflow uses deterministic mock/stub agent outputs, structured JSON handoff files, a phone-based shooting plan, self-written subtitles, and local editing. The submitted `outputs/final_video.mp4` is the self-edited final video, while `scripts/generate_video.py` remains a reproducible zero-paid-token fallback.

## Safety and copyright

- No API keys, tokens, passwords, or private credentials are included.
- No official logo is used because logo authorization was not confirmed.
- Identifiable people, if visible in the submitted self-edited video, must have consent recorded by the project author.
- Visuals in the fallback generator are self-made using Python/PIL; the submitted `outputs/final_video.mp4` is the final edited version.
- Department-related factual wording is limited to safe, general descriptions and official source references listed in `outputs/asset_sources.md`.

## Reproduce video on Linux

```bash
python3 scripts/generate_video.py
```

The script generates a fallback `outputs/final_video.mp4` and `outputs/subtitles.srt`. Do not run it after placing the final self-edited video unless you intentionally want to regenerate the fallback.
