from fastapi import FastAPI

from router.email_router import router as email_router
from services.email_service import EmailService
from repository.email_repository import EmailRepository

app = FastAPI(title="Email API")

app.state.email_service = EmailService(EmailRepository())

app.include_router(email_router)


@app.get("/")
def home():
    return {"message": "Email API is running"}