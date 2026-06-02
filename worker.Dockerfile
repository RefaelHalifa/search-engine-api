FROM python:3.11-slim

WORKDIR /worker

COPY worker.requirements.txt .
RUN pip install --no-cache-dir -r worker.requirements.txt

COPY worker/ ./worker/

CMD ["python3", "-m", "worker.main"]