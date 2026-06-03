# app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.elastic.client import create_index


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting search-engine-api")
    print(f"Elasticsearch: {settings.es_host}:{settings.es_port}")
    print(f"Kafka: {settings.kafka_bootstrap_servers}")
    await create_index()
    yield
    print("Shutting down search-engine-api")


app = FastAPI(
    title="Search Engine API",
    description="Mini-Google: document ingestion via Kafka, full-text and semantic search via Elasticsearch",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health():
    return {"status": "ok"}