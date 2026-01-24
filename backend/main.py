# main.py
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

