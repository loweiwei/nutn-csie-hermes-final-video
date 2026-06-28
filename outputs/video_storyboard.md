# Video Storyboard and Shooting Plan

This storyboard is optimized for a self-shot version of the NUTN CSIE 60-second promotional video. The Python/PIL generated video remains a fallback if real footage is not available.

| Scene | Time | Purpose | What To Shoot | Caption |
|---:|---|---|---|---|
| 1 | 0-5 sec | Opening hook | 打開筆電、鍵盤打字、螢幕顯示安全範例程式碼。用快速剪輯建立科技感。 | 在資訊工程的學習裡，一個想法可以從草稿開始，慢慢變成真的能運作的系統。 |
| 2 | 5-15 sec | Department identity | 校園或教學空間外觀、走廊/教室入口、乾淨背景加上「資訊工程學系」。 | 從程式設計出發，我們學習分析問題、拆解需求，並用技術做出清楚的解決方法。 |
| 3 | 15-30 sec | Learning fields | 螢幕程式碼、白板寫 AI / Data / System / Network、筆記或流程圖、demo 操作。 | 課程不只是在寫程式，也包含資料處理、人工智慧、系統設計、網路與各種實際應用。 |
| 4 | 30-45 sec | Practice and teamwork | 2-3 人圍著筆電討論、指著螢幕講解、白板畫專題流程、展示 demo。 | 透過專題實作和團隊合作，我們把課堂上的知識轉換成可以展示、可以改進的作品。 |
| 5 | 45-55 sec | Learning atmosphere | debug 畫面、checklist、白板修正、重新執行程式或儲存檔案。 | 每一次討論、測試和除錯，都是累積經驗的過程，也讓作品更接近完成。 |
| 6 | 55-60 sec | Closing call-to-action | 校園遠景、教室空景或筆電合上，最後加乾淨 title card。 | 在這裡，我們用程式連結創意與實作，讓資訊能力成為面向未來的力量。 |

## Detailed Shot List

### Scene 1 - Opening Hook, 0-5 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 1A | 1.5 sec | Close-up | 手打開筆電或碰觸鍵盤。 | 桌面不要出現私人文件。 |
| 1B | 1.5 sec | Close-up | 鍵盤打字或滑鼠操作。 | 不需拍到臉。 |
| 1C | 2 sec | Over-shoulder | 螢幕顯示安全範例程式碼或 demo。 | 不要拍到 API key、帳號、聊天視窗。 |

### Scene 2 - Department Identity, 5-15 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 2A | 4 sec | Wide | 校園或建築外觀。 | 避免路人臉部特寫。 |
| 2B | 3 sec | Medium | 走進教室、走廊或學習空間。 | 若有人入鏡需同意或避開。 |
| 2C | 3 sec | Static | 乾淨背景加上系名文字。 | 不使用未授權 logo。 |

### Scene 3 - Learning Fields, 15-30 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 3A | 4 sec | Close-up | 螢幕顯示簡單程式或專題 demo。 | 使用可公開範例。 |
| 3B | 4 sec | Medium | 白板寫 AI / Data / System / Network。 | 不寫未證實資訊。 |
| 3C | 3 sec | Insert | 筆記、流程圖或學習材料。 | 避免清楚拍攝有版權的整頁內容。 |
| 3D | 4 sec | Over-shoulder | 操作 demo 或資料視覺化。 | 避免私人資料。 |

### Scene 4 - Practice and Teamwork, 30-45 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 4A | 5 sec | Medium | 2-3 人圍著筆電討論。 | 可辨識人物需同意入鏡。 |
| 4B | 3 sec | Close-up | 手指向螢幕或流程圖。 | 可只拍手和螢幕降低肖像風險。 |
| 4C | 4 sec | Medium | 白板畫專題流程或系統圖。 | 內容保持通用。 |
| 4D | 3 sec | Static | 展示 demo 或簡報畫面。 | 不拍未公開資料。 |

### Scene 5 - Learning Atmosphere, 45-55 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 5A | 3 sec | Close-up | terminal、editor 或 debug 畫面。 | 裁掉 token、帳號、私人路徑。 |
| 5B | 2 sec | Insert | checklist、便條紙或待辦事項。 | 文字使用通用內容。 |
| 5C | 3 sec | Medium | 討論後修改白板或筆記。 | 人物需同意或避開臉。 |
| 5D | 2 sec | Close-up | 儲存檔案或重新執行程式。 | 不出現私人通知。 |

### Scene 6 - Closing, 55-60 sec

| Shot | Duration | Framing | Action | Safety |
|---|---:|---|---|---|
| 6A | 3 sec | Wide/Static | 校園遠景、教室空景或筆電合上。 | 畫面乾淨。 |
| 6B | 2 sec | Title card | 顯示 NUTN CSIE 與中文系名。 | 不使用未授權 logo。 |

## Editing Notes

- Total target length: 60 seconds; accepted range: 55-65 seconds.
- Shoot horizontally in 16:9.
- Keep subtitles readable: large white text with dark shadow or semi-transparent black background.
- Record every clip 2-3 seconds longer than needed.
- The final exported file should remain `outputs/final_video.mp4`.
- If self-shot footage is used, update `outputs/asset_sources.md` with filming source and consent notes.

## AI Video Generation Prompts

AI-generated video clips are optional. They are not required by the assignment, and the repo still keeps self-shot and Python/PIL fallback paths. If AI-generated clips are used, record the tool name, prompt summary, generation date, and usage rights in `outputs/asset_sources.md`.

Use 16:9 horizontal video. Generate each scene separately, then edit them together with the subtitles from `outputs/subtitles.srt`.

### Scene 1 - Opening Hook, 0-5 sec

**Duration:** 5 seconds

**Prompt:**

```text
A cinematic close-up sequence in a modern university classroom: a student's hands open a laptop, fingers type on a keyboard, and a computer screen shows clean sample programming code with no private data. Subtle blue technology light reflections, focused academic mood, realistic Taiwanese university setting, natural desk lighting, shallow depth of field, smooth camera push-in, 16:9 horizontal video, no logos, no brand names, no readable private information, no cyberpunk hacker stereotype.
```

**Negative prompt:**

```text
no passwords, no API keys, no private chat windows, no school logo, no exaggerated sci-fi, no hacker mask, no random English text errors, no distorted hands, no extra fingers
```

**Subtitle:** 在資訊工程的學習裡，一個想法可以從草稿開始，慢慢變成真的能運作的系統。

### Scene 2 - Department Identity, 5-15 sec

**Duration:** 10 seconds

**Prompt:**

```text
A clean establishing sequence of a Taiwanese university campus and learning space: exterior campus walkway in daylight, students walking in the distance, then a calm hallway or classroom entrance, ending on a clean background suitable for text overlay. The feeling is welcoming, academic, and professional. Realistic documentary style, stable camera, warm daylight, 16:9 horizontal video. Do not show official logos or emblems. Leave space in the center or lower third for the title text: National University of Tainan, Department of Computer Science and Information Engineering.
```

**Negative prompt:**

```text
no unauthorized logo, no close-up of identifiable strangers, no fake school emblem, no ranking claims, no English gibberish signs, no crowded commercial stock footage look
```

**Subtitle:** 從程式設計出發，我們學習分析問題、拆解需求，並用技術做出清楚的解決方法。

### Scene 3 - Learning Fields, 15-30 sec

**Duration:** 15 seconds

**Prompt:**

```text
A realistic montage showing computer science learning fields in a university environment: close-up of a laptop with sample code, a whiteboard with simple handwritten keywords AI, Data, System, Network, a notebook with a simple flowchart, and a student operating a clean demo interface or data visualization. Use smooth cuts between shots, bright classroom lighting, practical learning atmosphere, documentary promotional video style, 16:9 horizontal video. The scene should communicate programming, data, artificial intelligence, systems, networks, and applications without making rankings or equipment claims.
```

**Negative prompt:**

```text
no claim of top ranking, no fake laboratory equipment, no futuristic holograms, no private data, no unreadable corrupted text, no copyrighted textbook pages, no brand logos
```

**Subtitle:** 課程不只是在寫程式，也包含資料處理、人工智慧、系統設計、網路與各種實際應用。

### Scene 4 - Practice and Teamwork, 30-45 sec

**Duration:** 15 seconds

**Prompt:**

```text
A warm university project teamwork scene: two or three students collaborate around a laptop, one student points at a screen showing a simple demo, another sketches a system diagram on a whiteboard, then a short presentation-style moment showing a prototype interface. Realistic Taiwanese university classroom or study room, natural expressions, cooperative atmosphere, soft daylight, steady medium shots and close-up inserts, 16:9 horizontal video. Keep screens generic and safe, with no confidential information.
```

**Negative prompt:**

```text
no identifiable real person likeness, no private project data, no copyrighted UI, no school logo, no exaggerated celebration, no high-five stock cliché, no distorted faces or hands
```

**Subtitle:** 透過專題實作和團隊合作，我們把課堂上的知識轉換成可以展示、可以改進的作品。

### Scene 5 - Learning Atmosphere, 45-55 sec

**Duration:** 10 seconds

**Prompt:**

```text
A focused learning atmosphere sequence: close-up of a code editor or terminal with safe generic debug output, a paper checklist with simple tasks, students or hands revising a whiteboard diagram, and a final shot of running or saving code successfully. Realistic classroom desk setup, calm and determined mood, subtle camera movement, clean lighting, 16:9 horizontal video. The scene should show debugging, review, and improvement as part of learning.
```

**Negative prompt:**

```text
no API tokens, no usernames, no private file paths, no chat notifications, no error text containing real credentials, no chaotic screens, no cyber attack visuals
```

**Subtitle:** 每一次討論、測試和除錯，都是累積經驗的過程，也讓作品更接近完成。

### Scene 6 - Closing, 55-60 sec

**Duration:** 5 seconds

**Prompt:**

```text
A clean closing shot for a university computer science promotional video: quiet campus walkway or empty classroom in warm daylight, or a laptop gently closing on a desk, followed by a simple minimal title card with space for text. Calm, positive, professional ending, slow fade out, 16:9 horizontal video. Use text-only identity, no official logo or emblem.
```

**Negative prompt:**

```text
no unauthorized logo, no fake emblem, no incorrect website URL, no busy background, no random text artifacts, no distorted campus signs
```

**Subtitle:** 在這裡，我們用程式連結創意與實作，讓資訊能力成為面向未來的力量。

## AI Clip Editing Order

| Scene | Clip Length | Subtitle |
|---:|---:|---|
| 1 | 5 sec | 在資訊工程的學習裡，一個想法可以從草稿開始，慢慢變成真的能運作的系統。 |
| 2 | 10 sec | 從程式設計出發，我們學習分析問題、拆解需求，並用技術做出清楚的解決方法。 |
| 3 | 15 sec | 課程不只是在寫程式，也包含資料處理、人工智慧、系統設計、網路與各種實際應用。 |
| 4 | 15 sec | 透過專題實作和團隊合作，我們把課堂上的知識轉換成可以展示、可以改進的作品。 |
| 5 | 10 sec | 每一次討論、測試和除錯，都是累積經驗的過程，也讓作品更接近完成。 |
| 6 | 5 sec | 在這裡，我們用程式連結創意與實作，讓資訊能力成為面向未來的力量。 |

## AI Generation Notes

- Generate clips without embedded text if the tool often creates broken text; add Chinese subtitles later in the editor.
- Prefer realistic university documentary style over fantasy or cyberpunk visuals.
- Do not generate official NUTN logos, school emblems, fake rankings, fake lab names, or fake websites.
- If a generated clip contains distorted faces, strange hands, unreadable text, or random logos, regenerate or crop it out.
- Final export should still be named `outputs/final_video.mp4`.
