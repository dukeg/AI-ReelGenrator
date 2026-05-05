import os
from dotenv import load_dotenv

load_dotenv()

POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "3"))
APPROVAL_REQUIRED = os.getenv("APPROVAL_REQUIRED", "true").lower() == "true"
REEL_DURATION_SECONDS = 15
OUTPUT_DIR = "reels"
DATA_DIR = "data"

STYLE_PACKS = [
    "luxury fashion",
    "streetwear",
    "business look",
    "traditional outfit",
    "cyberpunk",
    "minimalist editorial",
    "sportswear",
    "party look",
    "royal theme",
    "cinematic portrait",
]

HOOKS = [
    "1 photo, 10 AI looks",
    "Wait for the final outfit",
    "AI changed the whole vibe",
    "Which style wins?",
    "This transformation is unreal",
    "Before vs AI glow-up",
    "The last look is premium",
    "AI fashion experiment",
    "From simple to cinematic",
    "Comment your favorite look",
]
