from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fuzzywuzzy import process
from google.cloud import speech
import json
import tempfile
import os
from google.cloud import speech
from google.oauth2 import service_account

#QuranDetect is stateless and privacy-first webapp.
client = speech.SpeechClient()
app = FastAPI(title="QuranDetect Full")

with open("quran_full.json", "r", encoding="utf-8") as f:
    quran_data = json.load(f)


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

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    #audio_content = await file.read()
    contents = await file.read()  # read the bytes
    audio = speech.RecognitionAudio(content=contents)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44000,
        language_code="ar-SA",
    )
    response = client.recognize(config=config, audio=audio)
    return {"transcript": response.results[0].alternatives[0].transcript}
'''
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=contents)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="ar-SA"
    )
    response = client.recognize(config=config, audio=audio)
    if len(response.results) == 0:
        return JSONResponse(content={"error": "No speech detected"}, status_code=400)
    transcript = response.result[0].alternatives[0].transcript
    confidence = response.results[0].alternatives[0].confidence
    match = match_ayah(transcript)
    if match:
        match["speech_confidence"] = confidence
        match["transcript"] = transcript
        return match
    else:
        return JSONResponse(content={"error": "No matching verse found"}, status_code=404)

'''

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



def match_ayah(transcript):
    choices = [item["arabic"] for item in quran_data]
    best_match, score = process.extractOne(transcript, choices)
    for item in quran_data:
        if item["arabic"] == best_match:
            return {
                "surah": item["surah"],
                "ayah": item["ayah"],
                "arabic": item["arabic"],
                "english": item["english"],
                "confidence": score
            }
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
