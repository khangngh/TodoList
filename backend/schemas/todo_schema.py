from pydantic import BaseModel, Field
from datetime import datetime


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)


class TodoUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    is_done: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime


class TodoListResponse(BaseModel):
    items: list[TodoResponse]
    total: int
    limit: int
    offset: int