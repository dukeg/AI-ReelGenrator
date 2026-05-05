from pathlib import Path

for d in ["input_images", "generated_assets", "reels", "captions", "data"]:
    Path(d).mkdir(exist_ok=True)

print("Project folders created.")
print("Place your image at: input_images/source.jpg")
