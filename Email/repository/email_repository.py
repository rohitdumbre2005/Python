import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from schemas.email_schema import EmailCreate

load_dotenv()

class EmailRepository:

    def __init__(self):
        pass

    def save_email(self, receiver_email: str, subject: str, body: str):
        """Save email details in the database.Implement database logic here if required."""
        return {"receiver_email": receiver_email, "subject": subject, "body": body}