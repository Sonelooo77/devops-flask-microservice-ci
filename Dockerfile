FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED = 1

COPY script.py .

CMD ["python3", "script.py"]
