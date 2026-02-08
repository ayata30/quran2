from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.speech import transcribe_audio
from utils.fuzzy_match import match_verse
from pydantic import BaseModel
import json
import os

app = FastAPI()

with open("quran_full.json", "r", encoding="utf-8") as f:
    quran_db = json.load(f)

app.add_middleware(
    CORSMiddleware,
   # allow_origins=["http://localhost:3000"],
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
async def detect(input: TextInput):
    matched = match_verse(input.text, quran_db)
    if matched:
        return matched

    return {"error": "No match"}



PORT = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)

    