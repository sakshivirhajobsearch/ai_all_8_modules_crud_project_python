from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def clip_analysis():
    return {"message": "CLIP multi-modal endpoint working"}
