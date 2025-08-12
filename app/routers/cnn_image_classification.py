# app/routers/cnn_image_classification.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_cnn():
    return {"message": "CNN Image Classification API is working"}
