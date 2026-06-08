# app/models/document.py
from datetime import datetime

from pydantic import BaseModel, Field


class DocumentIn(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime | None = Field(default_factory=datetime.utcnow)


class DocumentOut(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: datetime
    score: float | None = None