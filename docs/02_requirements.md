# Phase 2 – Requirement Analysis

## 1. Introduction

Requirement Analysis is the second phase of the FitBuddy project.

In this phase, the requirements of the application are identified and organized. The requirements describe what the system should do, what information it should accept, what output it should provide, and what technologies are required to build the application.

FitBuddy is designed to collect user fitness information, generate a personalized 7-day workout plan using Generative AI, provide a nutrition or recovery tip, store the generated information, and allow users to update their plans through feedback.

---

## 2. Project Objective

The main objective of FitBuddy is to develop a web-based AI fitness planning application that can generate personalized workout plans based on user information and fitness goals.

The system should:

- Collect basic user information.
- Collect the user's fitness goal.
- Collect the preferred workout intensity.
- Generate a personalized 7-day workout plan.
- Generate a nutrition or recovery tip.
- Allow users to provide feedback.
- Generate an updated plan based on feedback.
- Store user information and workout plans.
- Provide an administrative view of stored users and plans.

---

## 3. Functional Requirements

Functional requirements describe the operations that the FitBuddy application must perform.

### 3.1 User Registration and Input

The system must provide a form through which users can enter:

- Name
- User ID
- Age
- Weight
- Fitness goal
- Workout intensity

The information entered by the user is sent to the backend for processing.

---

### 3.2 Fitness Goal Selection

The application should allow the user to select a fitness goal.

Examples include:

- Weight loss
- Muscle gain
- General wellness

The selected goal is used when generating the workout plan and nutrition or recovery tip.

---

### 3.3 Workout Intensity

The user should be able to select the preferred workout intensity.

The supported intensity levels are:

- Low
- Medium
- High

The selected intensity is passed to the AI generation process.

---

### 3.4 Personalized Workout Generation

The system must generate a personalized 7-day workout plan based on the information provided by the user.

The generated plan should be organized by day and should provide structured workout information.

The project documentation describes workout content such as:

- Warm-up
- Main workout
- Exercises
- Sets and repetitions
- Cooldown or recovery guidance

---

### 3.5 Nutrition or Recovery Tip

The system should generate a concise nutrition or recovery tip related to the user's selected fitness goal.

For example, the application may provide general guidance related to hydration, protein, or recovery.

---

### 3.6 Feedback Submission

The system must allow the user to provide feedback about the generated workout plan.

Examples of feedback include:

- More focus on cardio
- Include more rest days
- Add yoga
- Modify the workout

---

### 3.7 Workout Plan Update

The system should process the user's feedback and generate an updated workout plan.

The original workout plan and the user's feedback are used as inputs for the AI-based update process.

The updated plan should be stored separately so that the original plan is also preserved.

---

### 3.8 Database Storage

The system must store user and workout information in a database.

The stored information includes:

- User ID
- Name
- Age
- Weight
- Fitness goal
- Workout intensity
- Original workout plan
- Updated workout plan

SQLite is used for persistent storage and SQLAlchemy is used for database interaction.

---

### 3.9 Admin View

The application should provide a dedicated view for administrators or coaches.

The admin view should allow stored user information and workout plans to be viewed.

The project documentation specifies that the admin view can display information such as:

- User name
- Age
- Weight
- Fitness goal
- Workout intensity
- Original workout plan
- Updated workout plan

---

### 3.10 API Support

The application should provide API endpoints for the major operations.

The API supports operations such as:

- Generating a workout plan
- Submitting feedback
- Viewing users
- Viewing individual user information

FastAPI is used to provide the backend API functionality.

---

## 4. Non-Functional Requirements

Non-functional requirements describe the qualities and characteristics expected from the application.

### 4.1 Usability

The application should provide a simple and understandable interface so that users can enter their information and receive their workout plan easily.

---

### 4.2 Performance

The application should process user requests efficiently and return generated results without unnecessary delay.

The AI model should be suitable for web-based interaction.

---

### 4.3 Reliability

The application should handle user input correctly and store generated information reliably in the database.

---

### 4.4 Maintainability

The application should use a modular structure so that different parts of the system can be maintained independently.

The project separates:

- Database operations
- AI generation
- Routes
- Schemas
- Configuration
- Frontend templates
- Static files

---

### 4.5 Security

Sensitive configuration information such as the Gemini API key should not be directly written into the source code.

Environment variables are used for configuration.

The `.env` file is used for local configuration and should not be committed to the public repository.

---

### 4.6 Compatibility

The application should run in a Python development environment and should be accessible through a modern web browser.

The FastAPI application can be run using Uvicorn.

---

## 5. Hardware Requirements

The application can be developed and tested using a normal computer.

Recommended basic requirements include:

- Computer or laptop
- Minimum 4 GB RAM
- Internet connection for Gemini API access
- Keyboard and mouse
- Modern web browser

---

## 6. Software Requirements

The following software and technologies are required:

| Software / Technology | Purpose |
|---|---|
| Python | Application programming |
| FastAPI | Backend framework |
| Uvicorn | Application server |
| Jinja2 | Dynamic HTML templates |
| SQLAlchemy | Database ORM |
| SQLite | Database |
| Google Gemini API | Generative AI |
| HTML | Frontend structure |
| CSS | Frontend styling |
| VS Code | Development environment |
| Git / GitHub | Version control and project submission |

---

## 7. AI Requirements

The AI component is responsible for generating fitness-related content.

The AI system should support:

### Workout Generation

Generate a structured 7-day workout plan based on:

- User information
- Fitness goal
- Workout intensity

### Nutrition / Recovery Generation

Generate a concise tip related to the selected fitness goal.

### Feedback-Based Updating

Use the original workout plan and user feedback to generate an updated plan.

The project documentation originally describes the use of Gemini Pro for workout generation and plan updates and Gemini Flash for quick nutrition tips. :contentReference[oaicite:1]{index=1}

---

## 8. Database Requirements

FitBuddy requires persistent storage for users and generated plans.

The database should store user information and plan information.

### User Information

The system stores:

- User ID
- Name
- Age
- Weight
- Goal
- Intensity

### Plan Information

The system stores:

- Original workout plan
- Updated workout plan
- Nutrition or recovery information

SQLite is selected because it provides a lightweight database suitable for the project.

---

## 9. Frontend Requirements

The application should provide an interactive web interface.

The main pages include:

### Home Page

Provides the form for entering user information.

### Result Page

Displays:

- User information
- Generated 7-day workout plan
- Nutrition or recovery tip
- Feedback form

### Admin Page

Displays registered users and their workout plans.

Jinja2 templates are used to dynamically display backend data in the HTML pages.

---

## 10. Backend Requirements

The backend is responsible for:

- Receiving user input.
- Validating input.
- Calling AI generation functions.
- Saving information to the database.
- Retrieving stored plans.
- Processing feedback.
- Generating updated plans.
- Rendering HTML templates.
- Providing API endpoints.

FastAPI is used as the backend framework.

---

## 11. User Scenarios

### Scenario 1 – Generate Workout Plan

A user enters their name, user ID, age, weight, fitness goal, and workout intensity.

The system processes the information and generates a personalized 7-day workout plan.

---

### Scenario 2 – Update Workout Plan

The user submits feedback about the existing plan.

The system uses the feedback to generate an updated workout plan.

---

### Scenario 3 – Nutrition or Recovery Tip

The user receives a concise nutrition or recovery tip based on their selected fitness goal.

---

### Scenario 4 – Admin View

An administrator or coach can view registered users and their original and updated workout plans.

These four scenarios are identified in the project documentation. :contentReference[oaicite:2]{index=2}

---

## 12. Input and Output Requirements

### Input

The application accepts:

```text
Name
User ID
Age
Weight
Fitness Goal
Workout Intensity
### Output

The application produces the following outputs:

- Personalized 7-day workout plan
- Daily workout activities
- Nutrition or recovery tip
- Updated workout plan based on user feedback
- Stored user and workout information

The generated information is displayed on the result page and stored in the SQLite database.

---

## 13. Constraints and Limitations

The FitBuddy application has some limitations.

- The quality of the generated plan depends on the AI model response.
- Gemini API access requires a valid API key when AI mode is enabled.
- An internet connection is required for Gemini API requests.
- The application provides general fitness guidance and is not a replacement for professional medical advice.
- The application does not diagnose medical conditions or prescribe medication.
- SQLite is suitable for this project but may not be suitable for a large-scale production system.

---

## 14. Conclusion

The Requirement Analysis phase identifies the functional, non-functional, hardware, software, AI, database, frontend, and backend requirements of the FitBuddy application.

The requirements provide a clear foundation for designing and developing the system. Based on these requirements, the next phase focuses on the overall architecture, database structure, application workflow, user interface, and AI integration of FitBuddy.
