FROM python:3.9.15-buster

RUN apt-get update
RUN apt-get install -y ffmpeg

WORKDIR /app

COPY app/requirements.txt .
COPY app/dl.py .

RUN pip install -r requirements.txt

CMD ["python3", "./dl.py"]
