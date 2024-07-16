from pydantic import BaseModel, EmailStr
from typing import List
from datetime import date

class CreateTripRequest(BaseModel):
    destination: str
    start_date: date
    end_date: date
    owner_name: str
    owner_email: EmailStr
    emails_to_invite: List[EmailStr]
