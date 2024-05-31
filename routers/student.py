from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.student import Student, StudentCreate
from crud.student import (get_student, get_students, create_student,
                          update_student, delete_student,
                          get_student_with_scores, get_students_with_scores)
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
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.get("/", response_model=list[Student])
def read_students(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    return get_students(db, skip=skip, limit=limit)


@router.get("/with-scores/", response_model=list[Student])
def read_students_with_scores(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    return get_students_with_scores(db, skip=skip, limit=limit)


@router.get("/{student_id}/with-scores", response_model=Student)
def read_student_with_scores(student_id: int, db: Session = Depends(get_db)):
    db_student = get_student_with_scores(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


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

