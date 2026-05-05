from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI(title="AI Reel Automation Dashboard")

@app.get("/")
def root():
    return {"status": "AI Reel Automation Dashboard running"}

@app.get("/plans")
def plans():
    p = Path("data/reel_plans.json")
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))

@app.get("/schedule")
def schedule():
    p = Path("data/schedule.json")
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))

@app.get("/health")
def health():
    return {"ok": True}
