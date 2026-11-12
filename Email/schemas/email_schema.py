from pydantic import BaseModel, Field, EmailStr

class EmailCreate(BaseModel):
    receiver_email: EmailStr
    subject: str = Field(min_length=2, max_length=200)
    body: str = Field(min_length=2, max_length=5000)