from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Введите значение оценки от 1 до 5"},
    )


async def validation_exception_handler(request: Request, exc: ValidationError):
    errors = exc.errors()
    for error in errors:
        if error['type'] in ['value_error.number.not_ge', 'value_error.number.not_le']:
            return JSONResponse(
                status_code=400,
                content={"detail": "Введите значение оценки от 1 до 5"},
            )
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )
