Set-ExecutionPolicy -Scope Process Bypass
python scripts/init_project.py
python app.py generate
python app.py render-samples
uvicorn dashboard.main:app --host 0.0.0.0 --port 8000
