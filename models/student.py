from pydantic import BaseModel

class Student(BaseModel):
    name: str
    email_address: str
    phone: str
