# Execution Trace

Project: NUTN CSIE 60-second promotional video  
Platform: Hermes Agent + Linux  
Run mode: zero-paid-token mock/stub execution trace  
Date: 2026-06-19

This trace documents the controlled multi-agent workflow. The assignment allows mock/stub agents and offline/dry-run traces when paid token or model resources are not used. The actual submitted artifacts are deterministic files in `agents/`, `handoff/`, `outputs/`, and `report/`.

## Environment

```bash
$ uname -a
Linux local-machine 6.x x86_64 GNU/Linux

$ python3 --version
Python 3.x

$ ffmpeg -version
ffmpeg installed
```

## Step 1 - Planner Agent

Input:
```text
Create a 60-second NUTN CSIE promotional video using Hermes Agent workflow.
Constraints: 55-65 seconds, zero paid token, no unverified claims, no official logo unless authorized.
```

Output:
```text
handoff/01_planner_output.json
```

Main result:
- Target audience: high school students, freshmen, parents, general viewers.
- Total length: 60 seconds.
- Six scenes were planned.
- Next tasks were delegated to Script, Visual, Reviewer, and Finalizer agents.

## Step 2 - Script Agent

Input:
```text
Read handoff/01_planner_output.json and write narration/subtitles.
```

Output:
```text
handoff/02_script_output.json
outputs/subtitles.srt
```

Main result:
- Six subtitle cues.
- No ranking, admission, employment, or unverified facility claims.
- Subtitles allow the video to be understood without voiceover.

## Step 3 - Visual Agent

Input:
```text
Read planner and script JSON files and design visual plan.
```

Output:
```text
handoff/03_visual_output.json
outputs/video_storyboard.md
```

Main result:
- Visual plan supports self-shot/self-edited footage as the primary path.
- No official logo, portrait, copyrighted image, or commercial video generation is required.
- Python/PIL video generation remains as a zero-paid-token fallback path.

## Step 4 - Reviewer Agent

Input:
```text
Review planner, script, and visual output.
```

Output:
```text
handoff/04_reviewer_feedback.json
```

Main result:
- Length: pass.
- Theme relevance: pass.
- Truthfulness: pass with conservative wording.
- Copyright: pass.
- Portrait rights: pass.
- Privacy: pass.
- Zero-paid-token feasibility: pass.

## Step 5 - Finalizer Agent

Input:
```text
Integrate Planner, Script, Visual, and Reviewer outputs.
```

Output:
```text
handoff/05_finalizer_output.json
README.md
outputs/asset_sources.md
```

Main result:
- Final video path confirmed: `outputs/final_video.mp4`.
- Report path confirmed: `report/Final_Report_NUTN_CSIE_Hermes.pdf`.
- Repo checklist completed.

## Step 6 - Final Video Export and Verification

```bash
$ ffprobe -v error -show_entries format=duration,size -show_entries stream=index,codec_type,codec_name,width,height -of default=noprint_wrappers=1 outputs/final_video.mp4
index=0
codec_name=h264
codec_type=video
width=1920
height=1080
index=1
codec_name=aac
codec_type=audio
duration=64.500000
size=30346401
```

Final result: the submitted video is `outputs/final_video.mp4`, a 64.5-second 1920x1080 MP4 with H.264 video and AAC audio. It is within the required 55-65 second range and below the recommended 100 MB size.

`scripts/generate_video.py` is retained only as a reproducible fallback generator. It should not be rerun after placing the self-edited final video unless the fallback version is intentionally regenerated.

## Final Artifacts

- `outputs/final_video.mp4`
- `outputs/subtitles.srt`
- `report/Final_Report_NUTN_CSIE_Hermes.pdf`
- `agents/*.md`
- `handoff/*.json`
- `baseline/single_agent_baseline.md`
- `outputs/asset_sources.md`
