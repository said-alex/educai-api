FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y make

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
