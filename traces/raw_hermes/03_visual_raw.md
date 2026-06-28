Query: # Visual / Media Agent

## Role
分鏡與素材規劃 agent。

## Responsibility
- 為每個 scene 設計 shot list、畫面元素、轉場與素材需求。
- 優先使用自製素材、手機拍攝、公開授權素材或程式生成影像。
- 為零付費 token 路徑設計可執行的 Linux/Python 影片生成方案。

## Input
`handoff/01_planner_output.json` and `handoff/02_script_output.json`

## Output
`handoff/03_visual_output.json` and `outputs/video_storyboard.md`

## Tool Policy
- 不使用未授權音樂、圖片、影片、字型或 logo。
- 不拍攝可辨識人物特寫，除非取得同意。
- 不把 AI 影片生成服務當成必要條件。

## Prompt
你是分鏡設計師。請為每個 scene 設計畫面、鏡頭、B-roll、轉場與素材來源。若沒有拍攝素材，請設計可由 Python/PIL 自製的視覺素材。輸出必須是 JSON。

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
Please output JSON only.
Initializing agent...
────────────────────────────────────────


╭─ ⚕ Hermes ───────────────────────────────────────────────────────────────────╮
    json
    {
      "project_info": {
        "topic": "NUTN CSIE 60-second promotional video",
        "platform_optimization": "Vertical (9:16)",
        "total_duration_seconds": 60
      },
      "visual_plan": [
        {
          "scene_number": 1,
          "duration_seconds": 8.0,
          "shot_list": [
            {
              "shot_id": "S1_01",
              "shot_type": "Extreme Close-up",
              "description": "Rapidly scrolling lines of Python/C++ code on a dark monitor with a subtle blue glow.",
              "movement": "Fast zoom-in",
              "transition": "Fast cut"
            },
            {
              "shot_id": "S1_02",
              "shot_type": "Macro",
              "description": "Abstract glowing circuit patterns (digital lines) moving through a 3D space.",
              "movement": "Panning",
              "transition": "Glitch effect"
            }
          ],
          "visual_elements": ["Code snippets", "Circuit overlays", "Blue/Cyan color palette"],
          "asset_requirements": [
            {
              "type": "Python-generated",
              "method": "Python/PIL/Manim",
              "description": "Procedural scrolling text of code and geometric circuit lines."
            },
            {
              "type": "Stock/B-roll",
              "description": "Close-up of glowing hardware LEDs."
            }
          ],
          "on_screen_text": "想知道科技如何改變未來嗎？",
          "source_strategy": "Self-generated via Python (Manim) for high-tech coding visuals to ensure zero-cost and professional look."
        },
        {
          "scene_number": 2,
          "duration_seconds": 15.0,
          "shot_list": [
            {
              "shot_id": "S2_01",
              "shot_type": "Wide Shot",
              "description": "The main campus building entrance or a representative academic building architecture.",
              "movement": "Slow tilt up",
              "transition": "Cross-dissolve"
            },
            {
              "shot_id": "S2_02",
              "shot_type": "Medium Shot",
              "description": "A student's hands typing on a laptop in a brightly lit, modern lab environment.",
              "movement": "Static",
              "transition": "Cut"
            }
          ],
          "visual_elements": ["Campus architecture", "Modern lab equipment", "Natural sunlight"],
          "asset_requirements": [
            {
              "type": "Mobile Shot",
              "description": "Phone-captured footage of NUTN campus buildings (User provided)."
            },
            {
              "type": "B-roll",
              "description": "Hands-on coding/hardware interaction."
            }
          ],
          "on_screen_text": "從理論到實作，掌握核心技術",
          "source_strategy": "Mobile photography for campus scenery; handheld B-roll for student interaction."
        },
        {
          "scene_number": 3,
          "duration_seconds": 12.0,
          "shot_list": [
            {
              "shot_id": "S3_01",
              "shot_type": "Split Screen",
              "description": "Left: Neural network graph animation. Right: Data points forming a cluster.",
              "movement": "Dynamic motion",
              "transition": "Slide"
            },
            {
              "shot_id": "S3_02",
              "shot_type": "Medium Shot",
              "description": "A digital visualization of a brain or a complex data structure node.",
              "movement": "Rotation",
              "transition": "Fade"
            }
          ],
          "visual_elements": ["Data nodes", "Neural network connections", "Mathematical symbols"],
          "asset_requirements": [
            {
              "type": "Python-generated",
              "method": "Matplotlib/Manim",
              "description": "Animated data science plots and neural network graph visualizations."
            }
          ],
          "on_screen_text": "探索 AI 與數據科學的前沿領域",
          "source_strategy": "Programmatic generation using Manim to create high-quality, zero-cost technical animations."
        },
        {
          "scene_number": 4,
          "duration_seconds": 10.0,
          "shot_list": [
            {
              "shot_id": "S4_01",
              "shot_type": "Medium Group Shot",
              "description": "A group of students sitting around a table, pointing at a screen and discussing enthusiastically.",
              "movement": "Handheld/Organic",
              "transition": "Cut"
            },
            {
              "shot_id": "S4_02",
              "shot_type": "Close-up",
              "description": "A high-five or a smile between two students in a campus lounge.",
              "movement": "Slow motion",
              "transition": "Dissolve"
            }
          ],
          "visual_elements": ["Collaborative setting", "Friendly atmosphere", "Natural campus lighting"],
          "asset_requirements": [
            {
              "type": "Mobile Shot",
              "description": "Candid student interaction/group study sessions (User provided)."
            }
          ],
          "on_screen_text": "在充滿活力的校園，遇見志同道合的夥伴",
          "source_strategy": "User-captured mobile footage of students to ensure authenticity and privacy compliance (with consent)."
        },
        {
          "scene_number": 5,
          "duration_seconds": 15.0,
          "shot_list": [
            {
              "shot_id": "S5_01",
              "shot_type": "Medium Shot",
              "description": "A student looking confidently into the camera and walking forward.",
              "movement": "Tracking shot",
              "transition": "Fade to Graphic"
            },
            {
              "shot_id": "S5_02",
              "shot_type": "Graphic/End Card",
              "description": "Clean minimalist background with the department's text and website URL.",
              "movement": "Static",
              "transition": "N/A"
            }
          ],
          "visual_elements": ["Clean typography", "Minimalist branding colors", "Call to action button style"],
          "asset_requirements": [
            {
              "type": "Python-generated",
              "method": "Python/PIL",
              "description": "High-resolution end-card with clean text layout and color gradients."
            }
          ],
          "on_screen_text": "加入南大資工，與我們一同定義未來！ [Website URL]",
          "source_strategy": "Python/PIL for the end-card to ensure perfect text alignment and professional resolution."
        }
      ]
    }
    
╰──────────────────────────────────────────────────────────────────────────────╯

Resume this session with:
  hermes --resume 20260621_214128_dc337c

Session:        20260621_214128_dc337c
Duration:       46s
Messages:       2 (1 user, 0 tool calls)
