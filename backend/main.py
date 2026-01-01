from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import os


app = FastAPI()



# The client gets the API key from the environment variable `GEMINI_API_KEY`.

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
# Allow your React frontend to communicate with the backend


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# main.py
quran_data = {}

with open("quran-simple-plain.txt", "r", encoding="utf-8") as f:
    for line in f:
        try:
            surah, ayah, arabic = line.strip().split("|")
            quran_data[arabic] = {
                "surah": int(surah),
                "ayah": int(ayah)
            }
        except ValueError:
            continue  # skip bad lines

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
    # Use Gemini API
    content = await file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[content.decode('utf-8')]  # adjust if you get bytes
    )
    return {"text": response.text}




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
