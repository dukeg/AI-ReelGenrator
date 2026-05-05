from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import numpy as np
from config import OUTPUT_DIR, REEL_DURATION_SECONDS

def _fit_916(img: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (720, 1280), (8, 8, 12))
    img = img.convert("RGB")
    img.thumbnail((720, 1280))
    x = (720 - img.width) // 2
    y = (1280 - img.height) // 2
    canvas.paste(img, (x, y))
    return canvas

def _draw_text(img: Image.Image, text: str, subtitle: str):
    draw = ImageDraw.Draw(img)
    try:
        font_big = ImageFont.truetype("arial.ttf", 44)
        font_small = ImageFont.truetype("arial.ttf", 26)
    except Exception:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.rectangle((30, 60, 690, 220), fill=(0, 0, 0))
    draw.text((50, 85), text[:34], fill=(255, 255, 255), font=font_big)
    draw.text((50, 160), subtitle[:52], fill=(220, 220, 220), font=font_small)

def render_sample_reels(image_path: str, plans):
    Path(OUTPUT_DIR).mkdir(exist_ok=True)

    src = Path(image_path)
    if not src.exists():
        base = Image.new("RGB", (720, 1280), (12, 12, 18))
        draw = ImageDraw.Draw(base)
        draw.text((80, 600), "Place source image at\ninput_images/source.jpg", fill=(255,255,255))
    else:
        base = _fit_916(Image.open(src))

    outputs = []
    for plan in plans:
        frames = []
        total_frames = 30 * REEL_DURATION_SECONDS

        for idx in range(total_frames):
            frame = base.copy()
            scale = 1 + min(idx, 120) * 0.0008
            crop_w = int(720 / scale)
            crop_h = int(1280 / scale)
            left = (720 - crop_w) // 2
            top = (1280 - crop_h) // 2
            frame = frame.crop((left, top, left + crop_w, top + crop_h)).resize((720, 1280))

            hook = plan["hook"] if idx < 90 else plan["style"].title()
            _draw_text(frame, hook, "AI reel concept")
            frames.append(np.array(frame))

        output = Path(OUTPUT_DIR) / f"reel_{plan['id']:03d}.mp4"
        imageio.mimsave(output, frames, fps=30)
        outputs.append(str(output))

    return outputs
