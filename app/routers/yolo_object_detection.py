from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def detect_objects():
    return {"message": "YOLO object detection endpoint working"}
