# Phase 7 – Project Documentation

## 1. Introduction

FitBuddy is an AI-based fitness plan generator developed using FastAPI, SQLite, Jinja2, HTML/CSS, and Google Gemini models.

The application collects basic user information such as name, user ID, age, weight, fitness goal, and workout intensity. Based on these inputs, the system generates a personalized 7-day workout plan and a nutrition/recovery tip.

The application also provides a feedback mechanism. Users can submit feedback about their generated plan, and the system can create an updated plan while preserving the original plan.

FitBuddy also includes an Admin / Coach View where stored user details, original plans, and updated plans can be reviewed.

---

## 2. Project Objectives

The main objectives of FitBuddy are:

- To collect basic fitness-related information from users.
- To generate personalized 7-day workout plans.
- To use Gemini models for AI-based fitness plan generation.
- To provide nutrition and recovery guidance.
- To allow users to submit feedback.
- To generate an updated plan based on user feedback.
- To preserve the original workout plan.
- To store user information and plans in SQLite.
- To provide an Admin / Coach View.
- To provide API endpoints for application functionality.
- To provide a simple and user-friendly interface.

---

## 3. Problem Statement

Creating a suitable workout plan manually can require time and knowledge about different fitness goals and workout levels.

Users may have different goals and preferred workout intensities. A single workout plan may not be suitable for everyone.

FitBuddy addresses this problem by collecting user information and generating a personalized workout plan based on the selected goal and intensity.

The feedback system also allows the generated plan to be updated according to user preferences.

---

## 4. Key Features

### 4.1 User Input

The application collects:

- Name
- User ID
- Age
- Weight
- Fitness Goal
- Workout Intensity

### 4.2 Personalized Workout Generation

FitBuddy generates a 7-day workout plan based on the information provided by the user.

The plan contains:

- Warm-up
- Main workout
- Training approach
- Cooldown
- Recovery days
- Safety information

### 4.3 Nutrition and Recovery Tip

The application provides a nutrition or recovery-related tip along with the workout plan.

### 4.4 Feedback System

Users can submit feedback about their generated plan.

The feedback can be used to modify the plan according to the user's preference.

### 4.5 Updated Workout Plan

After feedback is submitted, FitBuddy creates an updated version of the plan.

The original plan is preserved so that both versions can be reviewed.

### 4.6 Database Storage

User information and generated plans are stored using SQLite and SQLAlchemy.

### 4.7 Admin / Coach View

The Admin / Coach View allows stored users and their plans to be reviewed.

It displays:

- User details
- Original workout plan
- Updated workout plan
- Feedback information when available

### 4.8 API Support

FitBuddy provides API endpoints through FastAPI.

The API documentation can be accessed through the Swagger interface.

---

## 5. Technologies Used

The main technologies used in FitBuddy are:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend web framework |
| Uvicorn | Application server |
| Jinja2 | HTML template rendering |
| HTML | Frontend structure |
| CSS | Frontend styling |
| SQLite | Database |
| SQLAlchemy | Database interaction |
| Pydantic | Data validation |
| Google Gemini | AI-based plan generation |
| Pytest | Automated testing |
| Swagger / OpenAPI | API documentation |

---

## 6. System Architecture

The main architecture of FitBuddy is:

```text
                    User
                     |
                     v
              HTML / CSS UI
                     |
                     v
               FastAPI Routes
                     |
          +----------+----------+
          |                     |
          v                     v
     Validation             Database
      Pydantic            SQLite / SQLAlchemy
          |
          v
      AI Service
          |
          v
     Gemini Model
          |
          v
  Workout / Recovery Output
          |
          v
       Jinja2
          |
          v
      Result Page
      ## 7. Application Workflow

The overall FitBuddy workflow is:

1. The user opens the FitBuddy application.
2. The user enters their personal and fitness information.
3. FastAPI receives the submitted form.
4. Pydantic validates the input.
5. User information is stored in the SQLite database.
6. The workout generation service prepares the AI request.
7. Gemini is used when AI generation is enabled.
8. A 7-day workout plan is generated.
9. A nutrition/recovery tip is generated.
10. The generated information is stored in the database.
11. The result is displayed using the Jinja2 template.
12. The user can provide feedback.
13. The feedback is processed to create an updated plan.
14. The original plan remains preserved.
15. The Admin / Coach View displays stored user information and plans.

---

## 8. Project Folder Structure

The main project structure is:

```text
FitBuddy/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   └── all_users.html
│
├── static/
│   └── css/
│       └── style.css
│
├── tests/
│   └── test_app.py
│
├── docs/
│   ├── 01_brainstorming.md
│   ├── 02_requirements.md
│   ├── 03_project_design.md
│   ├── 04_project_planning.md
│   ├── 05_project_development.md
│   ├── 06_project_testing.md
│   └── 07_documentation.md
│
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── venv/