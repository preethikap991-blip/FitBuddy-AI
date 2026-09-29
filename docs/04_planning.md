# Phase 4 – Project Planning

## 1. Introduction

Project Planning is the fourth phase of the FitBuddy project.

The purpose of this phase is to organize the development activities, divide the project into milestones, assign responsibilities, identify deliverables, and plan the testing and deployment activities.

The FitBuddy project is divided into several development milestones so that the application can be developed and tested systematically.

---

## 2. Project Development Plan

The development of FitBuddy is planned in multiple stages.

The main stages include:

1. Model selection and project setup.
2. Backend and database development.
3. AI and Gemini API integration.
4. Frontend development.
5. Testing and debugging.
6. Local deployment.
7. Documentation and demonstration.

Each stage is completed and tested before moving to the next stage.

---

## 3. Project Milestones

### Milestone 1 – Model Selection and Environment Setup

The first milestone focuses on selecting the AI model and preparing the development environment.

Activities include:

- Selecting the Gemini model.
- Creating the project folder structure.
- Creating the Python virtual environment.
- Installing required dependencies.
- Configuring environment variables.
- Designing the basic application architecture.

---

### Milestone 2 – Core AI, Database and API Functionality

The second milestone focuses on developing the main backend functionality.

Activities include:

- Creating the database models.
- Configuring SQLite and SQLAlchemy.
- Creating Pydantic schemas.
- Developing the Gemini AI integration.
- Creating workout generation functionality.
- Creating nutrition or recovery tip generation.
- Creating feedback-based plan updating.
- Developing API endpoints.

---

### Milestone 3 – Routing Layer

The third milestone focuses on connecting the different components of the application.

Activities include:

- Creating FastAPI routes.
- Connecting routes with database operations.
- Connecting routes with AI generation functions.
- Processing user requests.
- Processing feedback submissions.
- Returning generated plans to the frontend.

---

### Milestone 4 – Frontend and User Interface

The fourth milestone focuses on creating the user interface.

Activities include:

- Creating Jinja2 HTML templates.
- Creating the home page.
- Creating the workout result page.
- Creating the feedback form.
- Creating the admin view.
- Adding responsive CSS styling.
- Connecting frontend forms with backend routes.

---

### Milestone 5 – Local Deployment and Testing

The fifth milestone focuses on running and testing the complete application.

Activities include:

- Running the application using Uvicorn.
- Testing the home page.
- Testing workout generation.
- Testing nutrition or recovery tips.
- Testing feedback submission.
- Testing updated workout plans.
- Testing database storage.
- Testing API endpoints.
- Testing the admin view.
- Fixing errors and validating the final application.

---

## 4. Suggested Team Division

The project work can be divided among four team members.

### Member 1 – Backend and API

Responsibilities:

- FastAPI application.
- Backend routes.
- API endpoints.
- Request and response handling.

### Member 2 – Gemini AI Integration

Responsibilities:

- Gemini API integration.
- Prompt design.
- Workout plan generation.
- Nutrition or recovery tip generation.
- Feedback-based plan updates.

### Member 3 – Frontend and UI

Responsibilities:

- HTML templates.
- Jinja2 integration.
- CSS styling.
- Forms.
- Result page.
- Admin interface.

### Member 4 – Database, Testing and Documentation

Responsibilities:

- SQLite database.
- SQLAlchemy models.
- Testing.
- Error checking.
- Project documentation.
- Demonstration preparation.

---

## 5. Technology Planning

The following technologies are planned for the project:

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | Backend framework |
| Uvicorn | Application server |
| Gemini API | Generative AI |
| SQLAlchemy | Database interaction |
| SQLite | Data storage |
| Jinja2 | HTML template rendering |
| HTML | Frontend structure |
| CSS | Frontend styling |
| VS Code | Development environment |
| Git / GitHub | Version control and project submission |

---

## 6. Project Deliverables

The planned project deliverables are:

- Complete source code.
- `requirements.txt` file.
- `.env.example` file.
- Test suite.
- Phase-by-phase project documentation.
- Demo video.
- Public GitHub repository.

---

## 7. Testing Plan

The application will be tested at different levels.

### Functional Testing

The main features will be tested to verify that they work correctly.

Examples include:

- User information submission.
- Workout plan generation.
- Nutrition or recovery tip generation.
- Feedback submission.
- Updated plan generation.
- Database storage.
- Admin view.

### API Testing

The FastAPI endpoints will be tested to verify that requests and responses are processed correctly.

### Database Testing

The database will be tested to ensure that user information and workout plans are stored and retrieved correctly.

### User Interface Testing

The frontend pages and forms will be tested using a modern web browser.

---

## 8. Risk Planning

Possible project risks include:

### Gemini API Availability

If the Gemini API is unavailable, AI generation may not work as expected.

### Invalid User Input

Incorrect or incomplete user information may cause validation problems.

### Database Errors

Database connection or storage problems may affect the application.

### Internet Connection

Gemini API access requires an internet connection.

### Integration Errors

Problems may occur when connecting the frontend, backend, database and AI services.

These risks will be reduced through validation, testing, error handling and proper configuration.

---

## 9. Deployment Plan

The application will first be developed and tested locally.

The planned local deployment process is:

1. Create a Python virtual environment.
2. Install the required dependencies.
3. Configure environment variables.
4. Initialize the database.
5. Start the FastAPI application using Uvicorn.
6. Open the application in a web browser.
7. Test all major features.

The application can later be prepared for deployment to a suitable hosting environment.

---

## 10. Project Schedule

The project activities are planned in the following order:

| Stage | Activity |
|---|---|
| 1 | Brainstorming and Ideation |
| 2 | Requirement Analysis |
| 3 | Project Design |
| 4 | Project Planning |
| 5 | Development |
| 6 | Testing |
| 7 | Documentation |
| 8 | Demonstration |

This sequence provides a structured approach for developing the FitBuddy application.

---

## 11. Final Project Deliverables

At the completion of the project, the following items should be available:

- Working FitBuddy web application.
- Backend source code.
- Frontend templates and CSS.
- Gemini AI integration.
- SQLite database.
- API endpoints.
- Automated tests.
- Requirements file.
- Environment configuration example.
- Phase documentation.
- Demonstration video.
- Public GitHub repository.

---

## 12. Conclusion

The project planning phase organizes the development of FitBuddy into clear milestones and responsibilities.

The planned approach covers AI integration, backend development, database management, frontend development, testing, deployment and documentation.

This planning provides a clear roadmap for completing the remaining phases of the FitBuddy project.