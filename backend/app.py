from openai import OpenAI
from fastapi  import FastAPI, File, UploadFile

app = FastAPI()
app.post("/transcribe")

# gonna use fastapi its the bets for globally scaled projects

# matching - rapis fuzz.
# quran data ---


client = OpenAI()
audio_file= open("/path/to/file/audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe", 
    file=audio_file
)

print(transcription.text)