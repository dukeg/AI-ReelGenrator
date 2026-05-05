import argparse
from pathlib import Path

from core.generator import generate_reel_plans
from core.renderer import render_sample_reels
from core.queue import load_plans, approve_items, schedule_approved

def ensure_dirs():
    for d in ["input_images", "generated_assets", "reels", "captions", "data"]:
        Path(d).mkdir(exist_ok=True)

def main():
    parser = argparse.ArgumentParser(description="AI Reel Automation System")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("generate")
    sub.add_parser("render-samples")

    approve = sub.add_parser("approve")
    approve.add_argument("--ids", nargs="+", type=int, required=True)

    sub.add_parser("schedule")

    args = parser.parse_args()
    ensure_dirs()

    if args.command == "generate":
        generate_reel_plans("input_images/source.jpg", count=100)
        print("Generated 100 reel plans in data/reel_plans.json")
    elif args.command == "render-samples":
        plans = load_plans()
        render_sample_reels("input_images/source.jpg", plans[:5])
        print("Rendered first 5 sample reels in reels/")
    elif args.command == "approve":
        approve_items(args.ids)
        print(f"Approved reels: {args.ids}")
    elif args.command == "schedule":
        schedule_approved()
        print("Created schedule in data/schedule.json")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
