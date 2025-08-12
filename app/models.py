from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class AIModel(Base):
    __tablename__ = "ai_models"
    id = Column(Integer, primary_key=True, index=True)
    model_type = Column(String, index=True)
    name = Column(String)
    description = Column(Text)
    result = Column(Text)
