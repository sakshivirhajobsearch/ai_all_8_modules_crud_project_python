from pydantic import BaseModel

class AIModelBase(BaseModel):
    name: str
    description: str

class AIModelCreate(AIModelBase):
    pass

class AIModelResponse(AIModelBase):
    id: int
    model_type: str
    result: str

    class Config:
       from_attributes = True
