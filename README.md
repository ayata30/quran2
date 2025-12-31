# QuranDetect

![QuranDetect Frontend Screenshot](assests\frontend.png)  

**Project Type:** Full-Stack Web Application | Backend / Web API | Python, FastAPI, PostgreSQL | Frontend: React + Tailwind CSS

## Description
QuranDetect is a Shazam-inspired web application that identifies Quran Surahs from user audio recordings.  
The frontend, built with React and Tailwind CSS, provides a responsive user interface for audio uploads and displays transcription results.  
The backend handles audio processing, relational database storage, and API integration for transcription and Surah retrieval.

## Features
- **Frontend:** React + Tailwind CSS for responsive, mobile-friendly UI that allows users to upload audio and view Surah results  
- **Backend:** RESTful API built with Python and FastAPI  
- **Database:** PostgreSQL for structured audio metadata storage  
- Audio processing and transcription using third-party APIs  
- Modular architecture for maintainability and scalability  
- Logging and environment-based configuration to support debugging and operational workflows  

## Tech Stack
**Frontend:** React, Tailwind CSS  
**Backend:** Python, FastAPI  
**Database:** PostgreSQL  
**Other:** Git, REST APIs

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
