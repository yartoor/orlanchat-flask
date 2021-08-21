FROM python:3.6-slim

COPY . /app

WORKDIR /app

RUN pip install -U pip && pip install -r requirements.txt

CMD python main.py
