from dataclasses import dataclasses

@dataclasses
class EmailCreate:
    receiver_email:str
    subject:str
    body:str