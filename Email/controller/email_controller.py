
from fastapi import Request, HTTPException
from schemas.email_schema import EmailCreate


class EmailController:

    def send_email(self, email: EmailCreate, request: Request):
        try:
            service = request.app.state.email_service
            service.send_email(email)

            return { "message": "Email has been successfully sent" }

        except Exception as exc:
            print("Email error:", repr(exc))
            raise HTTPException( status_code=500, detail=str(exc) ) from exc
