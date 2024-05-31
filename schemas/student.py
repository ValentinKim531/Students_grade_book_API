from typing import List
from pydantic import BaseModel
from datetime import datetime, date
from schemas.score import Score


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    birthdate: date
    email: str


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthdate: date
    email: str
    created_at: datetime
    updated_at: datetime
    scores: List[Score] = []

    class Config:
        from_attributes = True
