import requests

url = "https://qurandetect-backend-975745335288.us-central1.run.app/detect"

with open("sample.wav", "rb") as f:
    files = {"file": f}  # must be exactly "file" to match FastAPI
    res = requests.post(url, files=files, timeout=15)
    print(res.status_code)
    print(res.text)  # raw response



