# AI Reel Automation System

A safe creator automation system for generating reel plans, captions, sample reels, approval queues, schedules, and analytics.

## Features

- Generate 100 reel concepts from one image
- Create captions, hooks, hashtags, and AI prompts
- Produce sample vertical reels
- Approval queue before posting
- Safe scheduler
- Platform stubs for X, Instagram, and YouTube Shorts
- FastAPI dashboard API
- Docker-ready

## Quick Start

```bash
python -m venv .venv
pip install -r requirements.txt
python scripts/init_project.py
python app.py generate
python app.py render-samples
python app.py approve --ids 1 2 3
python app.py schedule
uvicorn dashboard.main:app --host 0.0.0.0 --port 8000
```

Place your image at:

```text
input_images/source.jpg
```

Open:

```text
http://localhost:8000/docs
```

## Docker

```bash
cp .env.example .env
docker compose up --build
```
