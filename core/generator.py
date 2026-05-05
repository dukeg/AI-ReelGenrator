import json
from pathlib import Path
from config import STYLE_PACKS, HOOKS, DATA_DIR

def generate_reel_plans(image_path: str, count: int = 100):
    Path(DATA_DIR).mkdir(exist_ok=True)
    Path("captions").mkdir(exist_ok=True)

    plans = []
    for i in range(count):
        style = STYLE_PACKS[i % len(STYLE_PACKS)]
        hook = HOOKS[i % len(HOOKS)]
        variation = i // len(STYLE_PACKS) + 1

        plans.append({
            "id": i + 1,
            "source_image": image_path,
            "style": style,
            "variation": variation,
            "hook": hook,
            "caption": (
                f"{hook}\n\n"
                f"Style: {style.title()} — Variation {variation}\n\n"
                "#AI #Fashion #Reels #AIEdits #ViralReels #CreativeAI"
            ),
            "image_prompt": (
                f"Transform the source image into a {style} look, ultra realistic, "
                f"vertical 9:16, premium Instagram reel style, cinematic lighting, "
                f"sharp details, social media ready."
            ),
            "video_prompt": (
                f"Create a 9:16 fashion transformation reel. Start with the original image, "
                f"then transition into {style}. Use quick flash transitions, smooth camera "
                f"push-in, premium lighting, viral social media style."
            ),
            "approved": False,
            "status": "draft"
        })

    Path(DATA_DIR, "reel_plans.json").write_text(json.dumps(plans, indent=2), encoding="utf-8")

    with Path("captions", "caption_bank.txt").open("w", encoding="utf-8") as f:
        for p in plans:
            f.write(f"REEL {p['id']}\n")
            f.write(f"HOOK: {p['hook']}\n")
            f.write(f"STYLE: {p['style']}\n")
            f.write(f"IMAGE PROMPT: {p['image_prompt']}\n")
            f.write(f"VIDEO PROMPT: {p['video_prompt']}\n")
            f.write(f"CAPTION:\n{p['caption']}\n")
            f.write("-" * 70 + "\n")

    return plans
