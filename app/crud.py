from sqlalchemy.orm import Session
from app import models, schemas

def create_ai_model(db: Session, model_type: str, model: schemas.AIModelCreate, result: str):
    db_model = models.AIModel(
        model_type=model_type,
        name=model.name,
        description=model.description,
        result=result
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def get_ai_models(db: Session, model_type: str):
    return db.query(models.AIModel).filter(models.AIModel.model_type == model_type).all()
