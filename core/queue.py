import json
from pathlib import Path
from datetime import datetime, timedelta
from config import DATA_DIR, POSTS_PER_DAY

PLANS_FILE = Path(DATA_DIR) / "reel_plans.json"
SCHEDULE_FILE = Path(DATA_DIR) / "schedule.json"

def load_plans():
    if not PLANS_FILE.exists():
        raise FileNotFoundError("Run `python app.py generate` first.")
    return json.loads(PLANS_FILE.read_text(encoding="utf-8"))

def save_plans(plans):
    PLANS_FILE.write_text(json.dumps(plans, indent=2), encoding="utf-8")

def approve_items(ids):
    plans = load_plans()
    id_set = set(ids)
    for p in plans:
        if p["id"] in id_set:
            p["approved"] = True
            p["status"] = "approved"
    save_plans(plans)

def schedule_approved():
    plans = load_plans()
    approved = [p for p in plans if p.get("approved")]

    schedule = []
    start = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    if start < datetime.now():
        start += timedelta(days=1)

    slot_gap_hours = max(1, int(24 / POSTS_PER_DAY))

    for idx, plan in enumerate(approved):
        day_offset = idx // POSTS_PER_DAY
        slot_offset = idx % POSTS_PER_DAY
        scheduled_at = start + timedelta(days=day_offset, hours=slot_offset * slot_gap_hours)
        schedule.append({
            "reel_id": plan["id"],
            "platforms": ["x", "instagram", "youtube_shorts"],
            "scheduled_at": scheduled_at.isoformat(),
            "status": "queued",
            "caption": plan["caption"],
            "video_file": f"reels/reel_{plan['id']:03d}.mp4"
        })

    SCHEDULE_FILE.write_text(json.dumps(schedule, indent=2), encoding="utf-8")
    return schedule
