# Email API – Python Project
## Project Overview
This project is a REST API developed using Python and FastAPI for email functionality.
It follows a layered architecture to separate routing, controllers, business logic, data handling, and request validation.
## Technologies Used
- Python
- FastAPI
- REST API
- Pydantic
- SMTP
- Gmail SMTP Server
## Project Structure
```text
Email/
├── controller/
│   └── email_controller.py
├── models/
│   └── email.py
├── repository/
│   └── email_repository.py
├── router/
│   └── email_router.py
├── schemas/
│   └── email_schema.py
├── services/
│   └── email_service.py
├── main.py
├── .gitignore
└── README.md
```
## Architecture
- Router: Handles API endpoints.
- Controller: Processes API requests.
- Service: Contains email business logic.
- Repository: Handles email-related operations.
- Models: Defines data structures.
- Schemas: Validates request data.
- Main: Initializes the FastAPI application.
## Configuration
Configure the following environment variables in your local `.env` file:
- EMAIL_ADDRESS
- EMAIL_APP_PASSWORD
Never upload `.env` or credentials to GitHub.
## Run the Application
Install dependencies:
```bash
pip install fastapi uvicorn python-dotenv
```
Install any additional dependencies required by the project.
Start the application:
```bash
python -m uvicorn main:app --reload --port 8081
```
API documentation:
http://127.0.0.1:8081/docs
## Author
Rohit Dumbre
GitHub: https://github.com/rohitdumbre2005
---
Python Development | REST API | Email Automation
