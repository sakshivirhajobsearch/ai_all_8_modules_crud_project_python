from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "CLIP Multi-modal API is running"}
