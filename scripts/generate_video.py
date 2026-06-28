#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np, subprocess, os, math

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "outputs"
SLIDES = OUT / "generated_slides"
SLIDES.mkdir(parents=True, exist_ok=True)

durations = [5, 10, 15, 15, 10, 5]
scenes = [
    {"title":"讓想法變成系統","subtitle":"在資訊時代，創意不只被看見，也能被實作。","caption":"在資訊工程的學習裡，一個想法可以從草稿開始，慢慢變成真的能運作的系統。"},
    {"title":"國立臺南大學 資訊工程學系","subtitle":"從程式設計出發，建立解決問題的基礎。","caption":"從程式設計出發，我們學習分析問題、拆解需求，並用技術做出清楚的解決方法。"},
    {"title":"不只寫程式","subtitle":"資料、人工智慧、系統、網路與應用，組成資訊工程的學習地圖。","caption":"課程不只是在寫程式，也包含資料處理、人工智慧、系統設計、網路與各種實際應用。"},
    {"title":"理論 × 實作 × 團隊","subtitle":"把課堂知識、專題實作與溝通協作串成完整能力。","caption":"透過專題實作和團隊合作，我們把課堂上的知識轉換成可以展示、可以改進的作品。"},
    {"title":"反覆討論，持續修正","subtitle":"在實驗、除錯與展示中，找到自己的技術方向。","caption":"每一次討論、測試和除錯，都是累積經驗的過程，也讓作品更接近完成。"},
    {"title":"歡迎認識 NUTN CSIE","subtitle":"一起把創意實作成未來。","caption":"在這裡，我們用程式連結創意與實作，讓資訊能力成為面向未來的力量。"},
]

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/arphic-bkai00mp/bkai00mp.ttf",
        "/usr/share/fonts/truetype/arphic-bsmi00lp/bsmi00lp.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if p and os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                continue
    return ImageFont.load_default()

def wrap_text(text, fnt, max_width):
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if ImageDraw.Draw(Image.new("RGB",(1,1))).textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines

def draw_centered(draw, y, text, fnt, fill, max_width=1080, line_gap=8):
    lines = wrap_text(text, fnt, max_width)
    total_h = sum(draw.textbbox((0,0), line, font=fnt)[3] - draw.textbbox((0,0), line, font=fnt)[1] for line in lines) + line_gap*(len(lines)-1)
    cy = y
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=fnt)
        w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        draw.text(((1280-w)/2, cy), line, font=fnt, fill=fill)
        cy += h + line_gap
    return total_h

def make_slide(idx, scene):
    W,H = 1280,720
    # Gradient background
    x = np.linspace(0,1,W)
    y = np.linspace(0,1,H)
    xx, yy = np.meshgrid(x,y)
    base = np.zeros((H,W,3), dtype=np.uint8)
    palettes = [
        ((10, 22, 55), (28, 88, 140)),
        ((20, 28, 66), (54, 100, 150)),
        ((15, 40, 70), (75, 110, 145)),
        ((30, 35, 65), (90, 86, 140)),
        ((20, 46, 60), (70, 118, 112)),
        ((12, 25, 55), (100, 130, 180)),
    ]
    c1,c2 = palettes[idx]
    for k in range(3):
        base[...,k] = (c1[k]*(1-xx*0.65-yy*0.20) + c2[k]*(xx*0.65+yy*0.20)).clip(0,255)
    img = Image.fromarray(base, "RGB")
    draw = ImageDraw.Draw(img, "RGBA")
    # Decorative circuit lines and nodes
    for i in range(12):
        y0 = 70 + i*48 + (idx%3)*5
        x0 = 50 + (i*91) % 400
        x1 = 1180 - ((i*73) % 250)
        alpha = 55 if i % 2 else 35
        draw.line((x0, y0, x1, y0 + ((i%3)-1)*28), fill=(180,220,255,alpha), width=2)
        for xnode in [x0, (x0+x1)//2, x1]:
            draw.ellipse((xnode-5,y0-5,xnode+5,y0+5), fill=(190,230,255,80))
    # Main translucent panel
    draw.rounded_rectangle((90,90,1190,590), radius=34, fill=(255,255,255,28), outline=(255,255,255,80), width=2)
    # Scene number
    draw.rounded_rectangle((110,112,235,154), radius=18, fill=(255,255,255,45))
    draw.text((132,121), f"SCENE {idx+1}", font=font(20, True), fill=(230,245,255,230))
    # Small code/card motifs
    if idx == 2:
        cards = ["Programming", "Data", "AI", "Systems", "Network"]
        for j, card in enumerate(cards):
            x0 = 145 + j*198
            y0 = 420
            draw.rounded_rectangle((x0,y0,x0+160,y0+72), radius=16, fill=(255,255,255,45), outline=(255,255,255,110))
            tw = draw.textlength(card, font=font(23, True))
            draw.text((x0+(160-tw)/2, y0+22), card, font=font(23, True), fill=(245,250,255,235))
    elif idx == 3:
        labels = ["Theory", "Practice", "Teamwork"]
        for j, lab in enumerate(labels):
            x0 = 255 + j*260
            y0 = 420
            draw.rounded_rectangle((x0,y0,x0+210,y0+76), radius=20, fill=(255,255,255,48), outline=(255,255,255,120))
            tw = draw.textlength(lab, font=font(25, True))
            draw.text((x0+(210-tw)/2, y0+23), lab, font=font(25, True), fill=(245,250,255,235))
            if j < len(labels)-1:
                draw.line((x0+215,y0+38,x0+255,y0+38), fill=(230,245,255,140), width=3)
                draw.polygon([(x0+255,y0+38),(x0+244,y0+30),(x0+244,y0+46)], fill=(230,245,255,140))
    elif idx == 4:
        # Debug console motif
        draw.rounded_rectangle((245,405,1035,500), radius=16, fill=(0,0,0,70), outline=(255,255,255,90))
        lines = ["> run project", "[review] improve", "[debug] fix", "[demo] show"]
        for j, line in enumerate(lines):
            draw.text((280,423+j*18), line, font=font(16), fill=(210,240,220,220))
    else:
        # Laptop / system motif
        draw.rounded_rectangle((455,405,825,490), radius=18, fill=(255,255,255,42), outline=(255,255,255,115))
        draw.rectangle((510,490,770,505), fill=(255,255,255,70))
        for j in range(4):
            draw.line((490,430+j*15,790,430+j*15), fill=(210,230,255,80), width=2)
    # Text
    draw_centered(draw, 205, scene["title"], font(52, True), (255,255,255,245), max_width=1050)
    draw_centered(draw, 315, scene["subtitle"], font(30), (236,246,255,230), max_width=930, line_gap=10)
    # Bottom caption bar
    draw.rounded_rectangle((110,620,1170,680), radius=20, fill=(0,0,0,95))
    draw_centered(draw, 637, scene["caption"], font(24, True), (255,255,255,240), max_width=980)
    return img

def write_srt():
    def ts(sec):
        return f"00:{sec//60:02d}:{sec%60:02d},000"
    cur = 0
    lines = []
    for i, (s, d) in enumerate(zip(scenes, durations), 1):
        lines += [str(i), f"{ts(cur)} --> {ts(cur+d)}", s["caption"], ""]
        cur += d
    (OUT/"subtitles.srt").write_text("\n".join(lines).strip()+"\n", encoding="utf-8")

def main():
    for i, s in enumerate(scenes):
        make_slide(i, s).save(SLIDES / f"slide_{i+1:02d}.png")
    write_srt()
    concat = OUT / "concat.txt"
    with concat.open("w", encoding="utf-8") as f:
        for i, d in enumerate(durations, 1):
            f.write(f"file '{(SLIDES / f'slide_{i:02d}.png').as_posix()}'\n")
            f.write(f"duration {d}\n")
        f.write(f"file '{(SLIDES / 'slide_06.png').as_posix()}'\n")
    output = OUT / "final_video.mp4"
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
        "-vf", "fps=30,format=yuv420p", "-t", "60",
        "-movflags", "+faststart", str(output)
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {output}")
    print(f"Generated {OUT/'subtitles.srt'}")

if __name__ == "__main__":
    main()
