# app/elastic/client.py
from elasticsearch import AsyncElasticsearch

from app.config import settings

es = AsyncElasticsearch(hosts=[f"http://{settings.es_host}:{settings.es_port}"])

INDEX_NAME = settings.es_index_documents

INDEX_MAPPING = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "title":      {"type": "text"},
            "content":    {"type": "text"},
            "author":     {"type": "keyword"},
            "created_at": {"type": "date"}
        }
    }
}


async def create_index() -> None:
    """Create the documents index in Elasticsearch if it doesn't already exist."""
    exists = await es.indices.exists(index=INDEX_NAME)
    if not exists:
        await es.indices.create(index=INDEX_NAME, body=INDEX_MAPPING)
        print(f"Index '{INDEX_NAME}' created.")
    else:
        print(f"Index '{INDEX_NAME}' already exists.")