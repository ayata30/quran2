from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import whisper
import tempfile
import os
from difflib import SequenceMatcher
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows frontend to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Whisper model once (this can take a few seconds)
model = whisper.load_model("base")

# Load Quran data
quran = []
with open("quran_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        surah, ayah, text = line.strip().split("|")
        quran.append({
            "surah": int(surah),
            "ayah": int(ayah),
            "text": text
        })

@app.get("/")
def home():
    return {"message": "QuranDetect local server running ✅"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language="ar")
    os.remove(tmp_path)
    return {"text": result["text"]}

@app.post("/detect")
async def detect_verse(request: dict):
    query = request.get("text")
    if not query:
        return {"error": "Missing text field"}

    best_match = None
    best_score = 0

    for verse in quran:
        score = SequenceMatcher(None, query, verse["text"]).ratio()
        if score > best_score:
            best_match = verse
            best_score = score

    return {"match": best_match, "confidence": round(best_score * 100, 2)}
