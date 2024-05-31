from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.score import Score, ScoreCreate
from crud.score import (get_score, get_scores, create_score,
                        update_score, delete_score)
from database import get_db

router = APIRouter()


@router.post("/", response_model=Score)
def create_new_score(score: ScoreCreate, db: Session = Depends(get_db)):
    try:
        return create_score(db, score)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{score_id}", response_model=Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = get_score(db, score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score


@router.get("/", response_model=list[Score])
def read_scores(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    return get_scores(db, skip=skip, limit=limit)


@router.patch("/{score_id}", response_model=Score)
def update_existing_score(
        score_id: int,
        score: ScoreCreate,
        db: Session = Depends(get_db)
):
    try:
        return update_score(db, score_id, score)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{score_id}", response_model=Score)
def delete_existing_score(score_id: int, db: Session = Depends(get_db)):
    try:
        return delete_score(db, score_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
