from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.speech import transcribe_audio
#from utils.fuzzy_match import match_verse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API is running!"}


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    transcript = transcribe_audio(audio_bytes)
    return {"text": transcript}

'''
@app.post("/detect")
async def detect(text: str):
    matched = match_verse(text, quran_db)
    if matched:
        return {"match": matched, "confidence": 95}  # calculate real confidence
    return {"match": None, "confidence": 0}
'''