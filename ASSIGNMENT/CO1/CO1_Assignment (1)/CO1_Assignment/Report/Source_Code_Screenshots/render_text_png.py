"""Renders a text file as a terminal-style PNG (used to produce the screenshot figures)."""
import sys
from PIL import Image, ImageDraw, ImageFont

def render(src, dst, title, width_chars=None):
    lines = open(src, encoding="utf-8").read().rstrip("\n").split("\n")
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 15)
    bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 15)
    cw = font.getlength("M")
    lh = 21
    maxlen = max(len(l) for l in lines) if lines else 40
    W = int(max(maxlen, len(title)) * cw + 60)
    H = int(len(lines) * lh + 90)
    img = Image.new("RGB", (W, H), "#1e1e1e")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 34], fill="#3c3c3c")
    for i, c in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        d.ellipse([12 + i * 20, 10, 24 + i * 20, 22], fill=c)
    d.text((W // 2 - len(title) * cw / 2, 9), title, font=font, fill="#cccccc")
    y = 46
    for l in lines:
        color = "#9cdcfe"
        if l.startswith("$"):
            color = "#6a9955"
        if "PASS" in l or "passed" in l or "Saved" in l:
            color = "#b5cea8"
        if "FAIL" in l:
            color = "#f48771"
        d.text((20, y), l, font=font, fill=color)
        y += lh
    img.save(dst)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], sys.argv[3])
