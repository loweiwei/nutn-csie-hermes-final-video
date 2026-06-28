Query: # Reviewer / Critic Agent

## Role
內容審查、風險檢查與 revision request agent。

## Responsibility
- 檢查影片長度是否 55-65 秒。
- 檢查是否符合 NUTN CSIE 主題。
- 檢查是否有事實風險、版權風險、肖像權風險與 privacy 風險。
- 產生具體修正要求。

## Input
`handoff/01_planner_output.json`, `handoff/02_script_output.json`, `handoff/03_visual_output.json`

## Output
`handoff/04_reviewer_feedback.json`

## Tool Policy
- 對所有具體主張保守處理。
- 未經確認的內容不可進入 final video。
- 若使用官方資訊，需列入素材來源表或報告來源。

## Prompt
你是內容審查者。請檢查這支 60 秒影片是否符合長度、主題、真實性、版權、肖像權與零付費 token 規範。請輸出 JSON review report，包含 pass/fail、risk list、revision request 與 final approval。

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
{
  "project_info": {
    "topic": "NUTN CSIE 60-second promotional video",
    "platform": "Hermes Agent on Linux",
    "target_audience": "Prospective university students (high schoolers), parents, and industry partners interested in tech talent.",
    "core_message": "NUTN CSIE offers a cutting-edge, practical, and innovation-driven environment for the next generation of tech leaders.",
    "total_duration_target_seconds": 60,
    "constraints": {
      "video_length_seconds": 60,
      "zero_paid_token": true,
      "use_official_logo": false,
      "avoid_unverified_claims": true
    }
  },
  "scenes": [
    {
      "scene_number": 1,
      "voiceover": "想知道科技如何改變未來嗎？",
      "subtitle": "想知道科技如何改變未來嗎？",
      "tone": "Energetic, inspiring",
      "start_time": 0.0,
      "end_time": 8.0
    },
    {
      "scene_number": 2,
      "voiceover": "在南大資工，我們不只學習理論，更在實作中掌握核心技術。",
      "subtitle": "從理論到實作，掌握核心技術",
      "tone": "Professional, reassuring",
      "start_time": 8.0,
      "end_time": 23.0
    },
    {
      "scene_number": 3,
      "voiceover": "探索人工智慧與數據科學，與頂尖研究並駕齊驅。",
      "subtitle": "探索 AI 與數據科學的前沿領域",
      "tone": "Intellectual, visionary",
      "start_time": 23.0,
      "end_time": 35.0
    },
    {
      "scene_number": 4,
      "voiceover": "在這裡，你將遇見志同道合的夥伴，在充滿活力的校園探索無限可能。",
      "subtitle": "在充滿活力的校園，遇見志同道合的夥伴",
      "tone": "Warm, welcoming",
      "start_time": 35.0,
      "end_time": 45.0
    },
    {
      "scene_number": 5,
      "voiceover": "加入南大資工，與我們一同定義未來。立即了解更多！",
      "subtitle": "加入南大資工，與我們一同定義未來！",
      "tone": "Direct, motivating",
      "start_time": 45.0,
      "end_time": 60.0
    }
  ]
}
{
  "project_title": "NUTN CSIE 60-second promotional video",
  "visual_style": "clean technology style, self-made vector-like slides, animated-information-system feeling",
  "resolution": "1280x720",
  "format": "MP4",
  "fps": 30,
  "scenes": [
    {
      "scene_id": 1,
      "time_range": "0-5",
      "shot_list": [
        "自製科技線條、流動節點、程式碼片段與主標題。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    },
    {
      "scene_id": 2,
      "time_range": "5-15",
      "shot_list": [
        "校名與系名文字標題、自製資訊節點與筆電示意圖。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    },
    {
      "scene_id": 3,
      "time_range": "15-30",
      "shot_list": [
        "五個自製資訊卡片：Programming / Data / AI / Systems / Network。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    },
    {
      "scene_id": 4,
      "time_range": "30-45",
      "shot_list": [
        "白板、專題流程、多人協作節點與 demo 介面示意。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    },
    {
      "scene_id": 5,
      "time_range": "45-55",
      "shot_list": [
        "debug console、review checklist、版本迭代箭頭。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    },
    {
      "scene_id": 6,
      "time_range": "55-60",
      "shot_list": [
        "收束標題、NUTN CSIE 字樣與簡潔 call-to-action。",
        "Use self-made shapes, nodes, cards, and code-like panels.",
        "Show subtitle/caption at the bottom for accessibility."
      ],
      "required_assets": [
        "Python/PIL generated slide",
        "self-made typography",
        "subtitle cue"
      ],
      "copyright_status": "self-made"
    }
  ],
  "fallback_plan": "If campus footage is available, replace generated slides with self-shot clips while keeping the same subtitles and timing."
}
Please output JSON only.
Initializing agent...
────────────────────────────────────────


╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
    json
    {
      "review_report": {
        "project_info": {
          "topic": "NUTN CSIE 60-second promotional video",
          "status": "Review In Progress"
        },
        "validation_results": {
          "duration_check": {
            "status": "pass",
            "calculated_duration_seconds": 60,
            "target_range": "55-65",
            "details": "Script and visual timelines align at 60 seconds."
          },
          "theme_check": {
            "status": "pass",
            "details": "Content focuses on NUTN CSIE academic strengths, technology (AI/Data Science), and community."
          },
          "compliance_check": {
            "status": "pass",
            "zero_paid_token_compliance": true,
            "copyright_safety": "High (Visuals rely on self-made Python/PIL assets and vector-like slides)",
            "privacy_and_portrait_rights": "High (Visuals use abstract nodes/graphics instead of real people, minimizing portrait risk)"
          }
        },
        "risk_assessment": {
          "risk_list": [
            {
              "type": "Fact/Claim Risk",
              "severity": "Low",
              "description": "Claims regarding 'top-tier research' and 'core technology' are subjective and should be presented as departmental focus rather than absolute global rankings unless cited.",
              "mitigation": "Use phrasing like 'focusing on' or 'exploring' rather than 'the best'."
            },
            {
              "type": "Verification Risk",
              "severity": "Medium",
              "description": "Final Call-to-Action (Scene 6) requires a verified URL to ensure prospective students land on the correct departmental page.",
              "mitigation": "Human verification of the official website URL before final export."
            }
          ]
        },
        "revision_requests": [
          {
            "scene_id": 3,
            "requirement": "Ensure that the mention of 'AI and Data Science' reflects the actual current curriculum emphasis of NUTN CSIE to avoid misleading applicants.",
            "priority": "Medium"
          },
          {
            "scene_id": 6,
            "requirement": "Provide/verify the specific official website URL for the Call-to-Action overlay.",
            "priority": "High"
          }
        ],
        "final_approval": {
          "status": "conditional_pass",
          "conditions": [
            "Verify official website URL",
            "Confirm curriculum alignment for AI/Data Science claims"
          ]
        }
      }
    }
    
╰──────────────────────────────────────────────────────────────────────────────╯

Resume this session with:
  hermes --resume 20260621_214214_561920

Session:        20260621_214214_561920
Duration:       23s
Messages:       2 (1 user, 0 tool calls)
