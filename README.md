# QuranDetect

**Project Type:** Full-Stack Web Application | Backend / Web API | Python, FastAPI | Frontend: React + Tailwind CSS

## Description
QuranDetect is a Shazam-inspired web application that identifies Quran Surahs from user audio recordings.  
The frontend, built with React and Tailwind CSS, provides a responsive user interface for audio uploads and displays transcription results.  


## Features
- **Frontend:** React + Tailwind CSS for responsive, mobile-friendly UI that allows users to upload audio and view Surah results  
- **Backend:** RESTful API built with Python and FastAPI   
- Audio processing and transcription using third-party APIs  
- Modular architecture for maintainability and scalability  
- Logging and environment-based configuration to support debugging and operational workflows  
<img width="2533" height="1319" alt="Screenshot 2026-02-05 101714" src="https://github.com/user-attachments/assets/05ed19e2-7e1e-4329-81b2-b191336c9124" />

🚀 Features

🎧 Upload Quran recitation audio

🗣️ Automatic Arabic speech transcription

📖 Fuzzy matching to identify Surah & Ayah

🌍 English translation included

⚡ FastAPI backend + React frontend
## Tech Stack
**Frontend:** React, Tailwind CSS  
**Backend:** Python, FastAPI  
**Other:** Git, REST APIs
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
