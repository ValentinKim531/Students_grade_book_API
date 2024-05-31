from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.student import Student, StudentCreate
from crud.student import (get_student, get_students, create_student,
                          update_student, delete_student)
from database import get_db

router = APIRouter()


@router.post("/", response_model=Student)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        return create_student(db, student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Ученик не найден")
    return db_student


@router.get("/", response_model=list[Student])
def read_students(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    return get_students(db, skip=skip, limit=limit)


@router.patch("/{student_id}", response_model=Student)
def update_existing_student(
        student_id: int,
        student: StudentCreate,
        db: Session = Depends(get_db)
):
    try:
        return update_student(db, student_id, student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{student_id}", response_model=Student)
def delete_existing_student(student_id: int, db: Session = Depends(get_db)):
    try:
        return delete_student(db, student_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


