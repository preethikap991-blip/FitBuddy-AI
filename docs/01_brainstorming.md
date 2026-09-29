# Phase 1 – Brainstorming & Ideation

## 1. Project Title

**FitBuddy – AI Fitness Plan Generator using Gemini Models**

---

## 2. Introduction

FitBuddy is an AI-powered web application designed to generate personalized fitness plans for users.

The application collects basic user information such as name, age, weight, fitness goal, and workout intensity. Based on these details, the system uses a Generative AI model to create a structured 7-day workout plan.

The application also provides nutrition or recovery tips and allows users to submit feedback so that the workout plan can be updated according to their requirements.

---

## 3. Problem Identification

Many people want to follow a regular fitness routine but may find it difficult to create a suitable workout plan.

Different users have different fitness goals and preferences. For example, one person may want to lose weight while another may want to improve general fitness or build strength.

Using the same workout plan for every user may not provide a personalized experience.

Therefore, there is a need for a simple system that can generate a fitness plan based on individual user information and goals.

---

## 4. Proposed Idea

The proposed solution is to develop **FitBuddy**, an AI-based fitness planning web application.

The application collects the user's fitness information and sends it to a Generative AI model. The AI generates a personalized 7-day workout plan based on the provided information.

The basic workflow is:

**User Information → Fitness Goal → Workout Intensity → AI Processing → 7-Day Workout Plan → Nutrition/Recovery Tip → User Feedback → Updated Plan**

---

## 5. Brainstorming of Possible Ideas

During the brainstorming stage, different approaches were considered.

### 5.1 Predefined Workout Plans

The first idea was to create fixed workout plans and display them to users.

For example:

- Monday – Cardio
- Tuesday – Strength Training
- Wednesday – Rest
- Thursday – Cardio
- Friday – Strength Training

However, fixed plans would not provide enough personalization.

### 5.2 Rule-Based Fitness Planner

Another idea was to use programming conditions.

For example:

- If the goal is weight loss, provide a cardio-focused plan.
- If the goal is muscle gain, provide a strength-focused plan.
- If the goal is general wellness, provide a balanced plan.

This approach would work for basic cases but would require many predefined rules.

### 5.3 AI-Based Fitness Planner

The final idea was to use Generative AI to create personalized workout plans.

The AI can process the user's information and generate a structured plan based on the user's goal and workout intensity.

This approach was selected for the FitBuddy project.

---

## 6. Selected Idea

The selected idea was an **AI-powered fitness plan generator**.

FitBuddy uses Generative AI to create personalized workout plans instead of depending only on fixed workout schedules.

The system also allows users to provide feedback and generate an updated plan.

---

## 7. Main Features Identified

The following features were identified during brainstorming:

### 7.1 User Information

The application collects:

- Name
- User ID
- Age
- Weight

### 7.2 Fitness Goal

Users can select their fitness goal, such as:

- Weight loss
- Muscle gain
- General wellness

### 7.3 Workout Intensity

The user can select the desired workout intensity.

### 7.4 AI-Generated Workout Plan

The system generates a personalized 7-day workout plan using Generative AI.

### 7.5 Nutrition and Recovery Tip

The system provides a useful nutrition or recovery suggestion related to the user's fitness goal.

### 7.6 Feedback

Users can provide feedback about their generated plan.

### 7.7 Updated Plan

The system uses the feedback to generate an improved or modified workout plan.

### 7.8 Database Storage

User information and generated plans are stored in a SQLite database.

### 7.9 Admin View

An admin view allows stored users and their plans to be viewed.

---

## 8. User Scenarios

### Scenario 1 – Generate a Workout Plan

The user enters their basic information and selects a fitness goal and workout intensity.

The system processes the information and generates a personalized 7-day workout plan.

### Scenario 2 – Give Feedback

After receiving the plan, the user can provide feedback.

For example:

> More focus on cardio.

The system uses the feedback to modify the workout plan.

### Scenario 3 – Receive an Updated Plan

The AI processes the user's feedback and generates an updated workout plan.

### Scenario 4 – Nutrition or Recovery Tip

The application provides a nutrition or recovery suggestion based on the user's selected fitness goal.

---

## 9. Technology Idea

The following technologies were identified for the project:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend framework and API |
| Gemini AI | Generative AI for fitness content |
| SQLite | Database |
| SQLAlchemy | Database interaction |
| Jinja2 | HTML template rendering |
| HTML | Web page structure |
| CSS | Web page styling |

---

## 10. Expected Benefits

The proposed FitBuddy application is expected to:

- Provide personalized workout plans.
- Reduce the effort required to create a basic fitness routine.
- Demonstrate the practical use of Generative AI.
- Provide nutrition and recovery suggestions.
- Allow users to modify plans through feedback.
- Store user and plan information.
- Provide a simple web-based user experience.

---

## 11. Project Scope

### Included in the Project

The project includes:

- User information collection
- Fitness goal selection
- Workout intensity selection
- AI-generated 7-day workout plans
- Nutrition and recovery tips
- Feedback submission
- Updated workout plans
- SQLite database storage
- Admin/user view
- API endpoints

### Outside the Project Scope

FitBuddy is designed as a general fitness planning application. It is not intended to replace a doctor, medical professional, qualified fitness trainer, or other professional advice.

---

## 12. Final Project Idea

The final project idea is:

**FitBuddy is an AI-powered web application that generates personalized 7-day fitness plans and nutrition or recovery tips based on user information and fitness goals. The system also allows users to provide feedback and receive updated plans.**

---

## 13. Conclusion

The brainstorming and ideation phase helped identify the problem of creating personalized fitness plans and led to the development of the FitBuddy concept.

After considering predefined plans, rule-based systems, and AI-based solutions, the AI-based approach was selected.

FitBuddy combines a web application, database, backend services, and Generative AI to provide a personalized fitness planning experience.

This idea forms the foundation for the remaining phases of the project.