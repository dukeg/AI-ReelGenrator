def post_to_youtube_shorts(video_path: str, title: str, description: str):
    print("DRY RUN: would upload YouTube Short")
    print(video_path)
    print(title)
    return {"platform": "youtube_shorts", "status": "dry_run"}
