Query: # Planner Agent

## Role
影音企劃與 workflow coordinator。

## Responsibility
- 定義短影片主題、受眾、核心訊息與 60 秒時間分配。
- 將影片拆解為 scenes。
- 指派 Script Agent、Visual Agent、Reviewer Agent、Finalizer Agent 的任務。
- 輸出 structured JSON，供下一個 agent 使用。

## Input
```json
{
  "topic": "NUTN CSIE 60-second promotional video",
  "platform": "Hermes Agent on Linux",
  "constraints": {
    "video_length_seconds": 60,
    "zero_paid_token": true,
    "use_official_logo": false,
    "avoid_unverified_claims": true
  }
}
```

## Output
`handoff/01_planner_output.json`

## Tool Policy
- 不使用 web search 作為自動化必要條件。
- 不連接 email、calendar、cloud drive 或社群帳號。
- 不讀取私人資料。
- 若資訊無法確認，標記為需要人工確認，不寫入影片主張。

## Prompt
你是短影音企劃 agent。請為「國立臺南大學資訊工程學系 60 秒形象宣傳影片」設計 55-65 秒內可完成的多場景結構。請明確標示目標觀眾、核心訊息、每個 scene 的時間、畫面、旁白方向、素材需求與風險。輸出必須是 JSON。

Input topic:
NUTN CSIE 60-second promotional video.
Please output JSON only.
Initializing agent...
────────────────────────────────────────

  ┊ 💻 preparing terminal…
  ┊ 💻 $         mkdir -p handoff  0.0s
  ┊ ✍️ preparing write_file…
  ┊ 💻 preparing terminal…
  ┊ 💻 $         cat << 'EOF' > handoff/01_planner_output.json
{
  "project_info": {
    "topic": "NUTN CSIE 60-second promotional video",
    "target_audience": "High school students, prospective university students, and parents interested in Computer Science and Engineering.",
    "core_message": "NUTN CSIE offers a dynamic learning environment, cutting-edge technology, and a supportive community to shape future tech leaders.",
    "platform_optimization": "Vertical (9:16) for TikTok/Reels/Shorts",
    "total_estimated_duration_seconds": 60
  },
  "workflow_plan": {
    "next_steps": [
      {
        "agent": "Script Agent",
        "task": "Generate a detailed 60-second script based on the scene breakdown, including spoken dialogue and text-on-screen overlays."
      },
      {
        "agent": "Visual Agent",
        "task": "Create visual descriptions, image/video generation prompts, and asset lists for each scene."
      },
      {
        "agent": "Reviewer Agent",
        "task": "Validate script and visual plan against constraints (length, zero-paid tokens, claim verification)."
      },
      {
        "agent": "Finalizer Agent",
        "task": "Consolidate all assets into a production-ready storyboard/timeline."
      }
    ]
  },
  "scenes": [
    {
      "scene_id": 1,
      "duration_seconds": 5,
      "hook_type": "Visual/Question",
      "visual_description": "Fast-paced montage of code scrolling, glowing circuit patterns, and a student looking intensely at a monitor.",
      "narration_direction": "Energetic and engaging. 'Ready to build the future?'",
      "on_screen_text": "Future Starts Here.",
      "asset_requirements": ["High-tech abstract motion graphics", "Close-up of coding screen"],
      "risks": "Must avoid generic 'hacker' tropes; keep it professional/academic."
    },
    {
      "scene_id": 2,
      "duration_seconds": 10,
      "hook_type": "Core Identity",
      "visual_description": "Wide shot of NUTN campus architecture transitioning into the CSIE department entrance/signage (generic architecture if official logo is not used).",
      "narration_direction": "Steady and welcoming. 'Welcome to NUTN Computer Science and Engineering.'",
      "on_screen_text": "NUTN CSIE",
      "asset_requirements": ["Campus scenery", "Department entrance"],
      "risks": "Ensure no unverified claims about rankings are made."
    },
    {
      "scene_id": 3,
      "duration_seconds": 15,
      "hook_type": "Academic Strength",
      "visual_description": "Split screen: 1. Students working in a modern lab. 2. A professor explaining a complex algorithm on a whiteboard.",
      "narration_direction": "Informative and authoritative. 'Advanced curriculum, hands-on labs, and expert guidance.'",
      "on_screen_text": "Innovation & Learning",
      "asset_requirements": ["Lab footage", "Whiteboard/Algorithm visuals"],
      "risks": "Need to confirm specific lab names or equipment availability with human verification."
    },
    {
      "scene_id": 4,
      "duration_seconds": 15,
      "hook_type": "Community/Culture",
      "visual_description": "Candid shots of students collaborating in a lounge, high-fiving after a hackathon, or working in small groups.",
      "narration_direction": "Warm and community-focused. 'Join a community of innovators and problem solvers.'",
      "on_screen_text": "Collaborative Culture",
      "asset_requirements": ["Student interaction footage", "Hackathon/Group study clips"],
      "risks": "Ensure all subjects in footage have permission or use stock-like representation."
    },
    {
      "scene_id": 5,
      "duration_seconds": 10,
      "hook_type": "Call to Action",
      "visual_description": "Final shot of a smiling student walking towards the camera, transitioning to a clean end screen with website info.",
      "narration_direction": "Inspiring and direct. 'Start your journey today at NUTN CSIE.'",
      "on_screen_text": "Apply Now | [Website URL]",
      "asset_requirements": ["Clean end-card graphic", "Student walking shot"],
      "risks": "Verify the URL is correct; flag as 'Needs Human Verification' if exact URL is unknown."
    },
    {
      "scene_id": 6,
      "duration_seconds": 5,
      "hook_type": "Outro",
      "visual_description": "Quick fade to black or departmental color gradient.",
      "narration_direction": "Silence / Soft musical swell.",
      "on_screen_text": "",
      "asset_requirements": ["Fade transition"],
      "risks": "N/A"
    }
  ],
  "constraints_check": {
    "max_length_seconds": 60,
    "calculated_length_seconds": 60,
    "zero_paid_tokens_compliance": true,
    "official_logo_usage": false,
    "unverified_claims_status": "Flagged for manual verification in Scene 3 and Scene 5."
  }
}
EOF
  0.0s

╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
    The planning phase is complete. I have defined the 60-second structure, scene breakdown, and handoff instructions for the subsequent agents.
    
    The output has been saved to:
    /home/vivian/Desktop/nutn_csie_hermes_final_project/handoff/01_planner_output.json
╰──────────────────────────────────────────────────────────────────────────────╯

Resume this session with:
  hermes --resume 20260621_213917_cab545

Session:        20260621_213917_cab545
Duration:       1m 30s
Messages:       8 (1 user, 6 tool calls)
