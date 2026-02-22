from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.speech import transcribe_audio
from utils.fuzzy_match import match_verse
from pydantic import BaseModel
import json
import os
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QURAN_PATH = os.path.join(BASE_DIR, "quran_full.json")

with open(QURAN_PATH, "r", encoding="utf-8") as f:
    quran_db = json.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
   allow_credentials=True,
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



class TextInput(BaseModel):
    text: str

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    logging.info(f"Received file: {file.filename}")
    try:
        audio_bytes = await file.read()
        logging.info(f"Read {len(audio_bytes)} bytes from audio")
        
        # Transcribe
        transcription = transcribe_audio(audio_bytes)
        logging.info(f"Transcription: {transcription}")
        
        # Match verse
        matched = match_verse(transcription, quran_db)
        logging.info(f"Matched: {matched}")

        if matched:
            return matched
        return {"error": "No match found"}

    except Exception as e:
        logging.error(f"Error processing file {file.filename}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))   

        