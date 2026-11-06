# FastAPI CI/CD Pipeline Demo

A hands-on project demonstrating how to build a REST API using **FastAPI** and automate software integration and delivery using **Git, GitHub and CI/CD workflows**.

## Overview

This repository demonstrates a practical development workflow for a Python FastAPI application, from local development and version control to automated pipeline execution.

The project is intended to demonstrate how development teams can maintain code quality, validate changes and manage feature development through Git branches and pull requests.

## Technology Stack

- **Python** – Backend programming language
- **FastAPI** – REST API framework
- **Git** – Version control
- **GitHub** – Source code management
- **GitHub Actions** – CI/CD workflow automation

## Project Objectives

1. Build and run a REST API using FastAPI.
2. Organise development using Git branches.
3. Maintain a separate feature branch for changes.
4. Automate validation through CI/CD workflows.
5. Demonstrate the pull request and merge workflow.
6. Understand how code changes trigger automated pipeline execution.

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI application

Replace `app.main:app` with the actual Python module path if your project uses a different structure.

```bash
uvicorn app.main:app --reload
```

### 5. Access the API

- API base URL: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Git Workflow

The project uses a feature-branch development approach.

### Branch structure

```text
main
  |
  └── feature/ci_cd_demo
```

- `main`: Primary branch of the repository.
- `feature/ci_cd_demo`: Development branch for implementing and testing changes.

### Create a feature branch

```bash
git switch main
git pull origin main
git switch -c feature/ci_cd_demo
```

### Commit and push changes

```bash
git add .
git commit -m "Add FastAPI CI-CD pipeline"
git push -u origin feature/ci_cd_demo
```

### Pull request workflow

1. Push the feature branch to GitHub.
2. Open a Pull Request targeting `main`.
3. Allow the configured CI/CD workflow to execute.
4. Review the pipeline results.
5. Merge the Pull Request after successful validation.

## CI/CD Workflow

The repository demonstrates how automated workflows can be connected to the Git development lifecycle.

The intended workflow is:

```text
Developer
    |
    v
Local Code Changes
    |
    v
Git Feature Branch
    |
    v
Push to GitHub
    |
    v
Pull Request to main
    |
    v
Automated CI/CD Workflow
    |
    v
Pipeline Validation
    |
    v
Review and Merge
```

The exact pipeline stages and deployment behaviour are defined by the workflow configuration in the repository.

## Project Structure

```text
project/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── <workflow-file>.yml
│
├── requirements.txt
├── .gitignore
└── README.md
```

*Update this structure to match the actual repository.*

## Learning Outcomes

By completing this project, learners will understand:

- FastAPI application development.
- Python virtual environments and dependency management.
- Git branching and remote repositories.
- Feature-based development.
- Pull requests and code integration.
- Automated CI/CD workflow execution.
- The relationship between source control and continuous integration.

## Future Enhancements

Potential extensions include:

- Automated unit and integration testing.
- Code quality and linting checks.
- Docker containerisation.
- Automated deployment to a cloud platform.
- Environment-specific configuration.
- Pipeline notifications and reporting.

## Author

**Jay Sanghavi**

AI Educator | Full-Stack Developer | AI Engineering

---

*This is a learning-oriented repository demonstrating practical backend development and CI/CD concepts.*