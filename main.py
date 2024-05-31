from fastapi import FastAPI
from routers import student, score
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(score.router, prefix="/scores", tags=["Scores"])