def post_to_x(video_path: str, caption: str):
    print("DRY RUN: would upload video to X")
    print(video_path)
    print(caption)
    return {"platform": "x", "status": "dry_run"}
