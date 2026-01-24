# main.py
'''
from fastapi import FastAPI, UploadFile, File
from pydub import AudioSegment
import io

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Qurandetect Backend (Speech-to-Text disabled for now)"}

@app.post("/upload-audio-test")
async def upload_audio_test(file: UploadFile = File(...)):
    """
    A test endpoint to confirm file upload and pydub processing works.
    Does NOT use Google Speech-to-Text.
    """
    try:
        # Read the uploaded file content
        audio_content = await file.read()

        # Use pydub to load the audio
        audio = AudioSegment.from_file(io.BytesIO(audio_content), format="mp3")

        # You can do a simple operation, e.g., get duration or export to WAV
        # For this test, let's just confirm it can be loaded and then return a success message
        duration_ms = len(audio)
        
        # Optionally, convert to WAV and save to a BytesIO object if you want to simulate the next step
        # wav_audio_io = io.BytesIO()
        # audio.export(wav_audio_io, format="wav")
        # wav_audio_io.seek(0) # Reset stream position

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": f"Audio file processed successfully by pydub. Duration: {duration_ms} ms. Speech-to-Text is currently disabled.",
            "status": "success"
        }
    except Exception as e:
        return {"message": f"Error processing audio: {str(e)}", "status": "error"}

'''
import json
from utils.fuzzy_match import match_verse

# Load Quran JSON
with open("quran_full.json", "r", encoding="utf-8") as f:
    quran_db = json.load(f)

# Example fuzzy test transcripts (simulate Google Speech API)
test_transcripts = [
    "بسم الله الرحمن الرحيم",                 # Exact
    "وَأَنَّا مِنَّا الصَّالِحُونَ وَمِنَّا دُونَ ذَٰلِكَ كُنَّا طَرَائِقَ قِدَدًا", # Exact
    "بسم الله الرحمٰن الرحيم",               # Slight variation
]

for transcript in test_transcripts:
    matched = match_verse(transcript, quran_db, threshold=50)
    if matched:
        print(f"Transcript: {transcript}")
        print(f"Matched Surah {matched['surah']}, Ayah {matched['ayah']}")
        print(f"Arabic: {matched['arabic']}")
        print(f"English: {matched['english']}\n")
    else:
        print(f"Transcript: {transcript} → No match found\n")

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# TODO(developer): Update and un-comment below line
PROJECT_ID = "qurandetect"

# Instantiates a client
client = SpeechClient()

# Reads a file as bytes
with open("resources/audio.wav", "rb") as f:
    audio_content = f.read()

config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    #encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.LINEAR16,
    #sample_rate_hertz=16000,
   # audio_channel_count=1,

    language_codes=["ar-SA"],
    model= "latest_short",

)

request = cloud_speech.RecognizeRequest(
    recognizer=f"projects/{PROJECT_ID}/locations/global/recognizers/_",
    config=config,
    content=audio_content,
)

# Transcribes the audio into text
response = client.recognize(request=request)

for result in response.results:
    print(f"Transcript: {result.alternatives[0].transcript}")