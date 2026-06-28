# 國立臺南大學資訊工程學系 60 秒形象宣傳影片

**學生／組員：** 羅暐媁  
**平台：** Hermes Agent + Linux  
**主題：** NUTN CSIE 60-second promotional video  
**影片檔案：** `outputs/final_video.mp4`  
**專案日期：** 2026-06-19

## 1. Project Title and Team Members

本專案題目為「國立臺南大學資訊工程學系 60 秒形象宣傳影片」。本作業選擇 **Hermes Agent + Linux** 作為主要 agent workflow 平台，設計一個可追蹤、可控制、可評估且不依賴付費 token 的多代理人短影片製作流程。組員為：羅暐媁。

## 2. Problem Definition

本次短影片目標是以約 60 秒向高中生、新生、家長與一般觀眾介紹「國立臺南大學資訊工程學系」。影片核心訊息是：資訊工程學習不只是寫程式，而是從程式設計、資料、人工智慧、系統、網路與應用出發，透過理論、實作與團隊合作，把創意轉化為可以運作的系統。

為避免不實或誇大內容，本影片不使用排名、錄取分數、就業率、招生名額、未確認設備或未授權 logo 等資訊。影片以手機實拍與字幕為主要製作方式，Python/PIL 自製視覺版本作為備案，因此不需要付費 AI 影音生成服務。

## 3. System Overview

本系統採用五個 specialized agents：

1. Planner Agent：負責主題定義、受眾、核心訊息、scene outline 與任務分派。
2. Script Agent：根據 planner output 撰寫旁白與字幕。
3. Visual Agent：設計每個 scene 的實拍鏡頭、素材需求、替代畫面與分鏡。
4. Reviewer Agent：檢查長度、真實性、版權、肖像權、螢幕隱私與零付費 token 可完成性。
5. Finalizer Agent：整合所有輸出，產生 final script、shooting list、字幕、素材表、repo checklist 與交付說明。

資料流如下：

```text
User topic
  -> Planner Agent
  -> 01_planner_output.json
  -> Script Agent + Visual Agent
  -> 02_script_output.json + 03_visual_output.json
  -> Reviewer Agent
  -> 04_reviewer_feedback.json
  -> Finalizer Agent
  -> 05_finalizer_output.json
  -> final_video.mp4 + report + README
```

## 4. Agent Design

| Agent | Input | Output | Responsibility |
|---|---|---|---|
| Planner | topic and constraints | `handoff/01_planner_output.json` | 拆解 60 秒影片任務、定義受眾、核心訊息與 scenes |
| Script | planner JSON | `handoff/02_script_output.json`, `outputs/subtitles.srt` | 撰寫旁白與字幕 |
| Visual | planner + script JSON | `handoff/03_visual_output.json`, `outputs/video_storyboard.md` | 設計畫面、shot list、素材需求 |
| Reviewer | planner + script + visual JSON | `handoff/04_reviewer_feedback.json` | 檢查長度、真實性、版權、肖像權與安全 |
| Finalizer | all previous JSON | `handoff/05_finalizer_output.json` | 整合交付內容與 repo checklist |

每個 agent 都有獨立 prompt、責任邊界、輸入格式、輸出格式與 tool policy，避免所有 agent 做同一件事。

## 5. Workflow Execution

本專案採用 zero-paid-token mock/stub execution。此路徑不需要商業 LLM API、不需要個人 API key，也不需要付費 AI 影片生成工具。所有 agent 中間產物都以 JSON 保存，完整紀錄於 `handoff/` 與 `traces/execution_trace.md`。

Agent workflow 檢查流程：

```bash
python3 scripts/run_mock_workflow.py
```

其中 `run_mock_workflow.py` 檢查所有 handoff JSON 是否存在且可讀；`outputs/video_storyboard.md` 提供可直接照拍的實拍分鏡。正式影片由學生自行剪輯後放置於 `outputs/final_video.mp4`。若無法完成實拍或需要零付費備案，`generate_video.py` 可使用 Python/PIL 產生自製視覺 slide，再透過 ffmpeg 匯出 MP4 作為 fallback。

## 6. Video Output

最終影片位於：

```text
outputs/final_video.mp4
```

影片規格：

- 長度：64.5 秒，符合 55 至 65 秒要求。
- 格式：MP4。
- 解析度：1920x1080。
- 影像／聲音：H.264 video with AAC audio。
- 字幕：影片內含文字字幕，另提供 `outputs/subtitles.srt` 作為字幕稿證據。
- 視覺素材：正式版本為學生自行剪輯影片；備案版本為 Python/PIL 自製，無外部圖片或影片依賴。
- 音樂／旁白：影片包含音訊；音樂或音效來源需記錄於 `outputs/asset_sources.md`，不得使用未授權商業音樂。

影片 scene 結構：

| Time | Purpose | Main Message |
|---|---|---|
| 0-5 | Opening hook | 想法從草稿開始，變成能運作的系統 |
| 5-15 | Problem solving | 從程式設計出發，學習分析問題與拆解需求 |
| 15-30 | Learning fields | 資料處理、人工智慧、系統設計、網路與應用 |
| 30-45 | Practice/teamwork | 透過專題實作與團隊合作，把知識轉成作品 |
| 45-55 | Learning atmosphere | 討論、測試與除錯，讓作品更接近完成 |
| 55-64.5 | Closing | 用程式連結創意與實作，面向未來 |

實拍版本的詳細鏡頭表位於 `outputs/video_storyboard.md`，包含每個 scene 的鏡頭大小、拍攝動作、建議秒數、字幕與安全注意事項。

## 7. Evaluation and Baseline Comparison

本專案建立了 `baseline/single_agent_baseline.md` 作為 single-agent baseline。比較結果如下：

| Criterion | Single-Agent Baseline | Multi-Agent Workflow |
|---|---|---|
| Structure | 容易混合企劃、腳本、分鏡與審查 | 每個 agent 有明確分工 |
| Traceability | 中間決策不容易追蹤 | 每一步以 JSON handoff 保存 |
| Safety Review | 容易忽略版權與真實性 | Reviewer Agent 明確檢查風險 |
| Revision | 修改範圍不清楚 | 可針對特定 agent output 修改 |
| Reproducibility | 依賴單次回答 | 有固定 repo 結構、trace、scripts 與 outputs |

因此，多代理人 workflow 比 single-agent baseline 更符合本作業重點：受控式流程、資料交接、execution trace、評估與可重現性。

## 8. Cost and Safety

### Zero-paid-token feasibility

本專案不依賴 paid token、商業 LLM API、個人 API key 或付費 AI 影音工具。所有 agent outputs 可由 mock/stub JSON 呈現；正式影片可由學生自行拍攝與剪輯完成，並保留本機 Linux + Python + ffmpeg 的 fallback 影片產生方式。

### Copyright and portrait rights

- 不使用官方 logo 或校徽。
- 不使用外部照片、影片、音樂或圖示，除非授權明確並列入素材表；本影片背景音訊使用 Canva 提供的免費音檔 `alexguz-funk-amp-breakbeat-541097.mp3`。
- 若拍攝可辨識人物，需取得同意。
- `outputs/asset_sources.md` 記錄正式影片、字幕、音訊、備案生成素材、引用來源與授權/同意注意事項。
- 所有引用來源均列於 `outputs/asset_sources.md`。

### Privacy

Repo 不包含 API key、token、password、私人帳號、學號、成績或敏感截圖。

## 9. Repository and Submission

正式繳交時需將本 repo 設為 Public，並在 Ecourse 繳交 repo 首頁完整連結。不要只交 GitHub profile、單一檔案連結、Google Drive 或 YouTube 連結。

建議 repo 名稱：

```text
nutn-csie-hermes-final-video
```

## 10. Reflection

本專案最大的重點不是追求昂貴模型或華麗 AI 生成，而是建立一個可以被助教檢查的 controlled multi-agent workflow。透過 Hermes Agent + Linux 的設計，本專案能清楚展示各 agent 的責任、資料交接、審查流程、影片輸出與零付費 token 可完成性。

本專案後續若要提升影片質感，可以進一步補強鏡頭穩定度、收音品質與字幕排版；但仍需保留相同的 agent handoff、execution trace、素材授權表與肖像權紀錄，確保影片品質提升不會破壞可追蹤性與安全要求。
