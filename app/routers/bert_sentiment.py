# app/routers/bert_sentiment.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "BERT Sentiment Analysis API is running"}
