from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    due_date: datetime | None = None
    tags: List[str] | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None
    due_date: datetime | None = None
    tags: List[str] | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    due_date: datetime | None
    tags: List[str] | None
    created_at: datetime
    updated_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True