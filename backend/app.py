from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
from difflib import SequenceMatcher
from dotenv  import load_dotenv
import json
import os
import uvicorn

load_dotenv()
print("OPENAI_API_KEY loaded:", os.getenv("OPENAI_API_KEY") is not None)


app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




# Load Quran dataset
with open("quran.json", "r", encoding="utf-8") as f:
    quran = json.load(f)

# Function to find best verse match
def find_best_match(query):
    best_match = None
    best_score = 0
    for verse in quran:
        score = SequenceMatcher(None, query, verse["text"]).ratio()
        if score > best_score:
            best_match = verse
            best_score = score
    return best_match, best_score

# 1️⃣ Transcription Endpoint
@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=file.file
        )
        return {"text": transcription.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2️⃣ Quran Detection Endpoint
@app.post("/detect")
async def detect_verse(data: dict):
    query = data.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="Missing 'query'")
    verse, score = find_best_match(query)
    if not verse:
        raise HTTPException(status_code=404, detail="No match found")
    return {"match": verse, "confidence": round(score * 100, 2)}

# Run the app (for local dev)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






# gonna use fastapi its the bets for globally scaled projects

# matching - rapis fuzz.
# quran data ---

#/transcrive - is the endpoint for getting audio into text
#/detect - endpoint for verse matching