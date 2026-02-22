<<<<<<< HEAD
FROM python:3.12-slim
=======
FROM python:3.11-slim
>>>>>>> c16d17795ab63ee09e946ddd8b6ac98a95a1fd18

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

<<<<<<< HEAD
EXPOSE 8080

CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}

=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
>>>>>>> c16d17795ab63ee09e946ddd8b6ac98a95a1fd18
