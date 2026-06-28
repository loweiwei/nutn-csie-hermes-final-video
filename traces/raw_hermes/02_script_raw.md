Query: # Script Agent

## Role
短影片腳本與字幕 agent。

## Responsibility
- 讀取 Planner Agent 的 scene outline。
- 撰寫旁白稿、字幕稿與每段 cue 的時間。
- 控制語氣正向、簡潔、適合高中生、新生、家長與一般觀眾。
- 避免誇大或未查證資訊。

## Input
`handoff/01_planner_output.json`

## Output
`handoff/02_script_output.json` and `outputs/subtitles.srt`

## Tool Policy
- 不創造未證實的排名、就業率、招生名額、師資或設備資訊。
- 不使用未授權的 slogan、官方 logo 或人物肖像。
- 旁白需能被字幕替代，確保無配音也能理解。

## Prompt
你是短影音腳本作者。請根據 Planner Agent 的 60 秒 outline，產生逐場景旁白、字幕、語氣與字幕時間。請輸出 JSON，且字幕總長必須落在 55-65 秒內。

Input:
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
Please output JSON only.
Initializing agent...
────────────────────────────────────────


╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
    json
    {
      "project_info": {
        "topic": "NUTN CSIE 60-second promotional video",
        "target_audience": "High school students, prospective university students, and parents interested in Computer Science and Engineering.",
        "core_message": "NUTN CSIE offers a dynamic learning environment, cutting-edge technology, and a supportive community to shape future tech leaders.",
        "total_estimated_duration_seconds": 60
      },
      "script": [
        {
          "scene_id": 1,
          "start_time": "00:00:00,000",
          "end_time": "00:00:05,000",
          "narration": "準備好打造未來了嗎？",
          "subtitle": "準備好打造未來了嗎？",
          "on_screen_text": "Future Starts Here.",
          "tone": "Energetic"
        },
        {
          "scene_id": 2,
          "start_time": "00:00:05,000",
          "end_time": "00:00:15,000",
          "narration": "歡迎來到南科大資工系。",
          "subtitle": "歡迎來到南科大資工系。",
          "on_screen_text": "NUTN CSIE",
          "tone": "Welcoming"
        },
        {
          "scene_id": 3,
          "start_time": "00:00:15,000",
          "end_time": "00:00:30,000",
          "narration": "在這裡，我們透過先進課程與實作實驗室，提供專業的技術指導。",
          "subtitle": "透過先進課程與實作實驗室，提供專業技術指導。",
          "on_screen_text": "Innovation & Learning",
          "tone": "Informative"
        },
        {
          "scene_id": 4,
          "start_time": "00:00:30,000",
          "end_time": "00:00:45,000",
          "narration": "加入充滿創新的社群，與夥伴們一起解決挑戰。",
          "subtitle": "加入充滿創新的社群，與夥伴們一起解決挑戰。",
          "on_screen_text": "Collaborative Culture",
          "tone": "Warm"
        },
        {
          "scene_id": 5,
          "start_time": "00:00:45,000",
          "end_time": "00:00:55,000",
          "narration": "今天就開始你的旅程，在南科大資工系實現夢想。",
          "subtitle": "今天就開始你的旅程，在南科大資工系實現夢想。",
          "on_screen_text": "Apply Now | [Website URL]",
          "tone": "Inspiring"
        },
        {
          "scene_id": 6,
          "start_time": "00:00:55,000",
          "end_time": "00:01:00,000",
          "narration": "",
          "subtitle": "",
          "on_screen_text": "",
          "tone": "Neutral"
        }
      ],
      "srt_content": "1\n00:00:00,000 --> 00:00:05,000\n準備好打造未來了嗎？\n\n2\n00:00:05,000 --> 00:00:15,000\n歡迎來到南科大資工系。\n\n3\n00:00:15,000 --> 00:00:30,000\n透過先進課程與實作實驗室，提供專業技術指導。\n\n4\n00:00:30,000 --> 00:00:45,000\n加入充滿創新的社群，與夥伴們一起解決挑戰。\n\n5\n00:00:45,000 --> 00:00:55,000\n今天就開始你的旅程，在南科大資工系實現夢想。"
    }
    
╰──────────────────────────────────────────────────────────────────────────────╯

Resume this session with:
  hermes --resume 20260621_214049_dcc044

Session:        20260621_214049_dcc044
Duration:       37s
Messages:       2 (1 user, 0 tool calls)
