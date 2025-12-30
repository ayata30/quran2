from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your React frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can replace * with "http://localhost:3000" later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "QuranDetect Backend is running!"}

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    with open(f"uploaded_{file.filename}", "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}


# ✅ example route we'll later connect to the frontend recorder
@app.post("/analyze-audio/")
async def analyze_audio():
    return {"result": "backend received the audio"}


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # For testing, just return dummy text
    # Later, integrate real transcription logic
    return {"text": "Bismillah ar-Rahman ar-Raheem"}

@app.post("/detect")
async def detect(data: dict):
    text = data.get("text", "")
    # Dummy detection logic
    return {
        "match": {
            "surah": 1,
            "ayah": 1,
            "text": "In the name of Allah, the Most Gracious, the Most Merciful"
        },
        "confidence": 99
    }
