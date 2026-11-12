
from fastapi import APIRouter, Request
from schemas.email_schema import EmailCreate
#from repository.email_repository import EmailRepository
from controller.email_controller import EmailController

router = APIRouter(
    prefix="/api/email",
    tags=["Email"]
)

controller = EmailController()

@router.post("/send")
def send_email(email: EmailCreate, request: Request):
    return controller.send_email(email, request)
