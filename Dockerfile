FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port=8080", "--host=0.0.0.0"]