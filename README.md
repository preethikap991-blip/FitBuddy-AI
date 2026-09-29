# FitBuddy – AI Fitness Plan Generator

A complete FastAPI + Jinja2 + SQLite + Gemini application based on the supplied FitBuddy project document.

## Features
- Responsive HTML/CSS frontend
- FastAPI backend
- SQLite + SQLAlchemy persistence
- Gemini-powered 7-day workout plan generation
- Gemini-powered nutrition/recovery tip
- Feedback-based plan regeneration
- Admin dashboard
- REST/JSON API endpoints
- Automatic demo mode when no Gemini API key is configured
- Basic automated tests

## Important model note
The supplied project document names Gemini 1.5 Pro and Gemini Flash. Those model names are no longer the safest defaults for a new project. This implementation keeps separate workout/tip model configuration but uses a current Gemini model through Google's current `google-genai` SDK. Change the model names in `.env` if your API account exposes another model.

## Project structure

```text
FitBuddy/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   └── all_users.html
├── static/
│   └── css/
│       └── style.css
├── tests/
│   └── test_app.py
├── docs/
│   ├── 01_brainstorming.md
│   ├── 02_requirements.md
│   ├── 03_design.md
│   ├── 04_planning.md
│   ├── 05_development.md
│   ├── 06_testing.md
│   ├── 07_documentation.md
│   └── 08_demonstration.md
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Windows VS Code setup

1. Install Python 3.11 or newer.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create the virtual environment:

```powershell
python -m venv venv
```

5. Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
venv\Scripts\activate
```

6. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

7. Copy `.env.example` to `.env`.

For Gemini mode, put your API key in `.env`:

```env
GEMINI_API_KEY=your_key_here
DEMO_MODE=false
```

For a no-key demo:

```env
DEMO_MODE=true
```

8. Start the application:

```powershell
uvicorn app.main:app --reload
```

9. Open:
- Website: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs
- Admin dashboard: http://127.0.0.1:8000/view-all-users

## Testing

With the virtual environment active:

```powershell
pytest -q
```

The tests use demo mode and do not require a Gemini API key.

## API endpoints

- `GET /health`
- `POST /api/generate-workout`
- `POST /api/submit-feedback/{user_id}`
- `GET /api/users`
- `GET /api/users/{user_id}`

The browser UI uses:
- `GET /`
- `POST /generate-workout`
- `POST /submit-feedback`
- `GET /view-all-users`

## Database

SQLite database file `fitbuddy.db` is created automatically on first run.

## Safety

FitBuddy is a software demonstration, not a medical or clinical system. AI output can be incorrect. Users should stop an exercise that causes pain and seek qualified professional advice for medical, injury, or condition-specific needs. The app does not calculate medical diets, diagnose conditions, or prescribe medication.

## GitHub phase submission

The `docs/` folder maps directly to the eight submission phases requested in the supplied project document. Add screenshots, diagrams, test evidence, and your own team information before submitting.
