# Phase 3 – Project Design

## 1. Introduction

Project Design is the third phase of the FitBuddy project.

In this phase, the overall architecture, modules, database structure, application workflow, frontend design, backend design, AI integration, and API structure of the FitBuddy application are defined.

The design is based on the requirements identified in Phase 2.

---

## 2. System Architecture

FitBuddy follows a web-based application architecture.

The major components of the system are:

- User Interface
- FastAPI Backend
- AI Service Layer
- Gemini API
- Database Layer
- SQLite Database

The overall architecture can be represented as:

User Browser
↓
FastAPI Routes
↓
AI Service Layer
↓
Gemini API

FastAPI Routes
↓
SQLAlchemy
↓
SQLite Database

FastAPI
↓
Jinja2 Templates
↓
HTML/CSS

The browser is used by the user to enter fitness information and view the generated plan.

FastAPI receives the request and processes the user information. The AI service layer communicates with the Gemini API to generate workout and recovery-related content.

SQLAlchemy is used to communicate with the SQLite database.

Jinja2 templates are used to generate the web pages dynamically.

---

## 3. System Workflow

The basic workflow of FitBuddy is:

1. The user opens the FitBuddy application.
2. The user enters their name, User ID, age, weight, fitness goal, and workout intensity.
3. The frontend sends the information to the FastAPI backend.
4. The backend validates the submitted information.
5. The AI service creates a structured prompt.
6. The Gemini model generates a 7-day workout plan.
7. A nutrition or recovery tip is generated.
8. The generated information is stored in the SQLite database.
9. The result is displayed to the user.
10. The user can submit feedback about the generated plan.
11. The feedback is processed by the backend.
12. An updated plan is generated.
13. The updated plan is stored in the database and displayed to the user.

---

## 4. Application Modules

The application is divided into multiple modules.

### 4.1 main.py

The `main.py` file creates the FastAPI application.

It is responsible for:

- Creating the FastAPI application.
- Configuring the application lifespan.
- Initializing the database.
- Connecting the application with the routes.

---

### 4.2 config.py

The `config.py` file manages application configuration.

It reads configuration values from environment variables.

Important configuration values include:

- Gemini API key
- Gemini model names
- Database URL
- Demo mode

This keeps configuration information separate from the main application code.

---

### 4.3 routes.py

The `routes.py` file contains the browser routes and API endpoints.

It handles:

- Displaying the home page.
- Generating workout plans.
- Displaying generated results.
- Receiving feedback.
- Generating updated plans.
- Displaying stored users.
- Providing API functionality.

---

### 4.4 schemas.py

The `schemas.py` file contains Pydantic schemas.

These schemas are used to:

- Validate user input.
- Define API request structures.
- Define expected data formats.

This helps prevent invalid data from being processed by the application.

---

### 4.5 database.py

The `database.py` file manages the database connection.

It contains:

- SQLAlchemy engine configuration.
- Database session creation.
- Database initialization.

SQLite is used as the database for the project.

---
### 4.6 models.py

The `models.py` file defines the database tables using SQLAlchemy.

The main models are:

- User
- Plan

These models represent the information stored in the SQLite database.

---

### 4.7 gemini_generator.py

The `gemini_generator.py` module is responsible for workout plan generation.

It receives user fitness information and creates a structured prompt for the Gemini model.

The generated response contains the user's 7-day workout plan.

---

### 4.8 gemini_flash_generator.py

The `gemini_flash_generator.py` module is used for generating a quick nutrition or recovery tip.

The generated tip is related to the user's fitness goal.

---

### 4.9 updated_plan.py

The `updated_plan.py` module handles feedback-based workout plan updates.

It uses:

- Original workout plan
- User feedback
- User fitness information

to generate an updated workout plan.

The original plan is preserved while the updated plan is stored separately.

---

## 5. Database Design

FitBuddy uses SQLite for persistent data storage.

SQLAlchemy is used as the Object Relational Mapping (ORM) layer.

The database contains two main tables:

### 5.1 Users Table

The `users` table stores basic user information.

Fields include:

- `id`
- `user_id`
- `username`
- `age`
- `weight`
- `goal`
- `intensity`
- `created_at`

---

### 5.2 Plans Table

The `plans` table stores generated workout information.

Fields include:

- `id`
- `user_id`
- `original_plan`
- `updated_plan`
- `nutrition_tip`
- `feedback`
- `created_at`
- `updated_at`

The plan information is associated with the corresponding user.

---

## 6. Frontend Design

The frontend provides a simple interface for interacting with FitBuddy.

The frontend uses:

- HTML
- CSS
- Jinja2 templates

### 6.1 Home Page

The home page provides the fitness information form.

The user enters:

- Name
- User ID
- Age
- Weight
- Fitness goal
- Workout intensity

The form is submitted to the FastAPI backend.

---

### 6.2 Result Page

The result page displays:

- User information
- 7-day workout plan
- Nutrition or recovery tip
- Feedback form

The page allows the user to provide feedback about the generated plan.

---

### 6.3 Admin View

The admin view displays stored user and plan information.

It allows the stored information to be viewed for project demonstration and administration purposes.

---

## 7. Backend Design

FastAPI is used as the backend framework.

The backend performs the following operations:

- Receives user input.
- Validates the input.
- Calls the AI generation modules.
- Saves information to the database.
- Retrieves stored information.
- Processes user feedback.
- Generates updated plans.
- Renders HTML pages.
- Provides API endpoints.

The backend acts as the main communication layer between the frontend, AI service, and database.

---

## 8. AI Integration Design

Generative AI is an important part of the FitBuddy system.

The application communicates with the Gemini API through the AI service modules.

### Workout Generation

User information is converted into a structured prompt.

The prompt is sent to the Gemini model to generate a 7-day workout plan.

### Nutrition / Recovery Tip

A separate AI generation process is used to produce a concise nutrition or recovery tip.

### Feedback-Based Update

When the user submits feedback, the original plan and feedback are provided to the AI generation process.

The system then generates an updated workout plan.

---

## 9. API Design

FitBuddy provides API endpoints through FastAPI.

The major API operations include:

### Generate Workout

```text
POST /api/generate-workouts