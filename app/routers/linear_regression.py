from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from app.ai_models import linear_regression_model

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AIModelResponse)
def run_linear_regression(model: schemas.AIModelCreate, db: Session = Depends(get_db)):
    result = linear_regression_model.train_and_predict(model.description)
    return crud.create_ai_model(db, "Linear Regression", model, result)

@router.get("/", response_model=list[schemas.AIModelResponse])
def get_all_linear_models(db: Session = Depends(get_db)):
    return crud.get_ai_models(db, "Linear Regression")
