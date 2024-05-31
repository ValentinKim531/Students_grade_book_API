from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from routers import student, score
from database import engine, Base
from validation.exception_handlers import request_validation_exception_handler, validation_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(ValidationError, validation_exception_handler)

app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(score.router, prefix="/scores", tags=["Scores"])