from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your React frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can replace * with "http://localhost:3000" later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "QuranDetect Backend is running!"}

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    with open(f"uploaded_{file.filename}", "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}
# ✅ test route
@app.get("/ping")
def ping():
    return {"message": "pong"}

# ✅ example route we'll later connect to the frontend recorder
@app.post("/analyze-audio/")
async def analyze_audio():
    return {"result": "backend received the audio"}