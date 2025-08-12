from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

from app.routers import (
    linear_regression,
    cnn_image_classification,
    bert_sentiment,
    gan,
    q_learning,
    yolo_object_detection,
    clip_multimodal,
    alphafold
)
import uvicorn

app = FastAPI(title="AI CRUD for All Models")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Favicon route
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join("static", "favicon.ico"))

# Root HTML page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>AI CRUD Project</title>
            <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
        </head>
        <body>
            <h1>Welcome to AI CRUD for All Models</h1>
            <ul>
                <li><a href="/docs#/Linear%20Regression">Linear Regression</a></li>
                <li><a href="/docs#/CNN%20Image%20Classification">CNN Image Classification</a></li>
                <li><a href="/docs#/BERT%20Sentiment%20Analysis">BERT Sentiment Analysis</a></li>
                <li><a href="/docs#/GAN">GAN</a></li>
                <li><a href="/docs#/Q-Learning">Q-Learning</a></li>
                <li><a href="/docs#/YOLO%20Object%20Detection">YOLO Object Detection</a></li>
                <li><a href="/docs#/CLIP%20Multi-Modal">CLIP Multi-Modal</a></li>
                <li><a href="/docs#/AlphaFold">AlphaFold</a></li>
            </ul>
        </body>
    </html>
    """

# Register routers with prefixes and tags
app.include_router(linear_regression.router, prefix="/linear", tags=["Linear Regression"])
app.include_router(cnn_image_classification.router, prefix="/cnn", tags=["CNN Image Classification"])
app.include_router(bert_sentiment.router, prefix="/bert", tags=["BERT Sentiment Analysis"])
app.include_router(gan.router, prefix="/gan", tags=["GAN"])
app.include_router(q_learning.router, prefix="/qlearning", tags=["Q-Learning"])
app.include_router(yolo_object_detection.router, prefix="/yolo", tags=["YOLO Object Detection"])
app.include_router(clip_multimodal.router, prefix="/clip", tags=["CLIP Multi-Modal"])
app.include_router(alphafold.router, prefix="/alphafold", tags=["AlphaFold"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
