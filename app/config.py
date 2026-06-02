from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_port: int = 8000
    secret_key: str

    kafka_bootstrap_servers: str
    kafka_topic_documents: str

    es_host: str
    es_port: int
    es_index_documents: str

    class Config:
        env_file = ".env"


settings = Settings()