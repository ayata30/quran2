from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, UploadFile, File
import tempfile

from google.cloud import speech

#QuranDetect is stateless and privacy-first.

app = FastAPI()

# main.py
# " quran_data = {}
"""
with open("quran-simple-plain.txt", "r", encoding="utf-8") as f:
    for line in f:
        try:
            surah, ayah, arabic = line.strip().split("|")
            quran_data[arabic] = {
                "surah": int(surah),
                "ayah": int(ayah)
            }
        except ValueError:
            continue  # skip bad lines """

@app.get("/")
def home():
    return {"message": "QuranDetect Backend is running!"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    client = speech.SpeechClient()

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    with open(tmp_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ar-SA",
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    return {"text": transcript}

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    with open(f"uploaded_{file.filename}", "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}



@app.post("/detect")
async def detect(data: dict):
    text = data.get("text", "").strip()
    english_text = get_translation(match["surah"], match["ayah"])


    # Exact match first
    if text in quran_data:
        match = quran_data[text]
        return {
            "match": {
                "surah": match["surah"],
                "ayah": match["ayah"],
                "arabic_text": text,
                 "english_text": english_text
                
            },
            "confidence": 100
        }
    
    # Optional: Fuzzy match if transcription not exact
    from difflib import get_close_matches
    closest = get_close_matches(text, quran_data.keys(), n=1, cutoff=0.7)
    if closest:
        match = quran_data[closest[0]]
        return {
            "match": {
                "surah": match["surah"],
                "ayah": match["ayah"],
                "arabic_text": closest[0],
                
            },
            "confidence": 80
        }

    return {
        "match": None,
        "confidence": 0,
        "message": "No match found"
    }

import requests

def get_translation(surah, ayah):
    url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad"
    r = requests.get(url).json()
    return r['data']['text'] if r.get('data') else ""
