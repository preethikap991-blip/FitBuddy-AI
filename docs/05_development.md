# Phase 5 – Project Development

## 1. Introduction

Project Development is the fifth phase of the FitBuddy project.

In this phase, the planned design and requirements are converted into a working application.

The development process includes the frontend, backend, database, Generative AI integration, feedback system, and testing support.

---

## 2. Development Environment

The FitBuddy application was developed using the following environment:

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS
- Google Gemini API
- Pydantic
- VS Code

A Python virtual environment is used to manage the project dependencies.

---

## 3. Project Structure

The project is organized into separate folders and files.

### Main Application Files

- `main.py` – Creates and starts the FastAPI application.
- `config.py` – Manages application configuration and environment variables.
- `database.py` – Creates the database engine and database sessions.
- `models.py` – Defines the database models.
- `schemas.py` – Defines and validates user input.
- `routes.py` – Contains browser and API routes.
- `gemini_generator.py` – Generates workout plans using Gemini.
- `gemini_flash_generator.py` – Generates nutrition or recovery tips.
- `updated_plan.py` – Generates an updated plan based on feedback.

### Frontend

The frontend uses:

- Jinja2 templates.
- HTML.
- CSS.

The main templates include:

- `base.html`
- `index.html`
- `result.html`
- `all_users.html`

---

## 4. Development Flow

The main development flow of FitBuddy is:

1. The browser displays the FitBuddy input form.
2. The user enters their fitness information.
3. The browser sends the form data to the FastAPI backend.
4. FastAPI validates the data through the `UserInput` schema.
5. User information is inserted or updated in SQLite.
6. The workout prompt is created using the user's information.
7. The prompt is sent to the configured Gemini model.
8. A separate prompt is used to generate a nutrition or recovery tip.
9. The generated information is stored in the database.
10. The `result.html` page displays the generated results.
11. The user can submit feedback about the generated plan.
12. The original plan and feedback are sent to the plan update process.
13. Gemini generates an updated plan based on the feedback.
14. The updated plan is stored separately.
15. The original plan is preserved for reference.

---

## 5. Backend Development

FastAPI is used to develop the backend of the application.

The backend is responsible for:

- Receiving user input.
- Validating user data.
- Calling AI generation functions.
- Storing information in SQLite.
- Processing feedback.
- Generating updated plans.
- Rendering HTML pages.
- Providing API endpoints.

The backend acts as the communication layer between the frontend, database, and AI services.

---

## 6. Database Development

SQLite is used as the database for FitBuddy.

SQLAlchemy is used to communicate with the SQLite database.

The project contains two main database models:

### User

The User model stores information such as:

- User ID
- Name
- Age
- Weight
- Fitness goal
- Workout intensity
- Creation date

### Plan

The Plan model stores:

- Original workout plan
- Updated workout plan
- Nutrition or recovery tip
- User feedback
- Creation date
- Updated date

This allows the application to preserve the original plan while also storing updated versions.

---

## 7. Generative AI Integration

Generative AI is an important component of FitBuddy.

The application uses Gemini models to generate fitness-related content.

### Workout Generation

The user's information is converted into a structured prompt.

The prompt contains information such as:

- Age
- Weight
- Fitness goal
- Workout intensity

The prompt is sent to the configured Gemini model to generate a 7-day workout plan.

---

### Nutrition / Recovery Tip

A separate AI generation process is used to create a concise nutrition or recovery tip.

The tip is related to the user's selected fitness goal.

---

### Feedback-Based Plan Update

After viewing the generated plan, the user can provide feedback.

The application sends the original plan together with the user's feedback to the update process.

The updated plan is then generated and stored separately from the original plan.

---

## 8. Frontend Development

The frontend is developed using HTML, Jinja2 and CSS.

### Home Page

The home page allows the user to enter:

- Name
- User ID
- Age
- Weight
- Fitness goal
- Workout intensity

The form sends the information to the FastAPI backend.

### Result Page

The result page displays:

- User information
- 7-day workout plan
- Nutrition or recovery tip
- Feedback form
- Updated workout plan when available

### Admin View

The admin view displays stored user and plan information.

---

## 9. API Development

FastAPI provides API endpoints for the main application operations.

The implemented API operations include:

- Generate a workout plan.
- Submit feedback.
- View all users.
- View an individual user's information.

The API allows the backend functionality to be accessed programmatically in addition to the browser-based interface.

---

## 10. Feedback System

The feedback system allows users to request changes to their generated workout plan.

For example, a user may provide feedback such as:

- More focus on cardio.
- Add more rest.
- Include yoga.
- Modify the workout.

The feedback is processed along with the original plan to generate an updated plan.

The original plan is not overwritten.

---

## 11. Demo Mode

FitBuddy includes a demo mode to make development and testing easier.

When:

`DEMO_MODE=true`

or when the Gemini API key is not available, the application can return deterministic local output instead of making a network AI request.

This allows the application to be tested locally without requiring a Gemini API call.

Demo mode is useful for:

- Development.
- Testing.
- Demonstration.
- Debugging.
- Offline testing.

---

## 12. Error Handling and Validation

Input validation is performed before processing user information.

The application uses Pydantic schemas to validate incoming data.

This helps prevent invalid information from being processed by the backend.

The application also separates configuration, database operations, routes, and AI generation into different modules, making errors easier to identify and maintain.

---

## 13. Local Application Execution

The completed application can be run locally using Uvicorn.

The application is started using:

```text
uvicorn app.main:app --reload