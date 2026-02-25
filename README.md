# QuranDetect

**Project Type:** Full-Stack Web Application | Backend: Python, FastAPI | Frontend: React + Tailwind CSS  | Tools: Google Speech to Text API, Docker

## Description
QuranDetect is a Shazam-inspired web application that identifies Quran Ayahs from user audio recordings. The user is able to upload their audio and immeditaely get a text repsonse back of the corrcelty located Ayah.  
 
<img width="2533" height="1367" alt="Screenshot 2026-02-24 203056" src="https://github.com/user-attachments/assets/963372c8-661d-403e-b243-7202a1661884" />


## 🚀 Features

🎧 Upload Quran recitation audio

🗣️ Automatic Arabic speech transcription

📖 Fuzzy matching to identify Surah & Ayah

🌍 English translation included

This project combines my interest in software engineering and meaningful real-world applications. It’s an ongoing project focused on learning full-stack development, APIs, and deployment.

## Installation / Setup
```bash
# Clone repo
git clone https://github.com/ayata30/Quran2.git
cd qurandetect-frontend  # your local folder name

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend setup
cd ../frontend
npm install
npm start
<img width="2555" height="1331" alt="image" src="https://github.com/user-attachments/assets/fe097d38-5a0e-496e-ae4a-9cfb224c0328" />
