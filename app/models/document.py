# app/models/document.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class DocumentIn(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class DocumentOut(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: datetime
    score: Optional[float] = None