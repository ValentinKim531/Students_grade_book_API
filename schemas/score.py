from pydantic import BaseModel
from datetime import datetime


class ScoreCreate(BaseModel):
    student_id: int
    score: int


class Score(BaseModel):
    id: int
    student_id: int
    score: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
