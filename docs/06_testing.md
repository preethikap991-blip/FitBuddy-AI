# Phase 6 – Project Testing

## 1. Introduction

Project Testing is the sixth phase of the FitBuddy project.

The purpose of this phase is to verify that the application works correctly and that the major components of the system work together without errors.

Testing is performed using both automated tests and manual testing.

---

## 2. Testing Objectives

The main objectives of testing are:

- Verify that the application starts correctly.
- Verify that the home page loads successfully.
- Verify that user input is validated.
- Verify that workout plans can be generated.
- Verify that nutrition or recovery tips are generated.
- Verify that user information is stored.
- Verify that feedback can be submitted.
- Verify that updated plans are generated.
- Verify that the original plan remains preserved.
- Verify that API endpoints work correctly.
- Verify that the admin view displays stored information.

---

## 3. Automated Testing

Automated tests are included in the `tests` folder.

The test suite can be executed using:

```bash
pytest -q