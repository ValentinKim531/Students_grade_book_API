from sqlalchemy.orm import Session
from models.score import Score
from schemas.score import ScoreCreate

def get_score(db: Session, score_id: int):
    return db.query(Score).filter(Score.id == score_id).first()

def get_scores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Score).offset(skip).limit(limit).all()

def create_score(db: Session, score: ScoreCreate):
    db_score = Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, score: ScoreCreate):
    db_score = get_score(db, score_id)
    if db_score:
        for key, value in score.dict().items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = get_score(db, score_id)
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
