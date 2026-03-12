# from pydantic import BaseModel, Field
# from datetime import datetime


# class TodoCreate(BaseModel):
#     title: str = Field(..., min_length=3, max_length=100)


# class TodoUpdate(BaseModel):
#     title: str = Field(..., min_length=3, max_length=100)
#     is_done: bool


# class TodoResponse(BaseModel):
#     id: int
#     title: str
#     is_done: bool
#     created_at: datetime


# class TodoListResponse(BaseModel):
#     items: list[TodoResponse]
#     total: int
#     limit: int
#     offset: int

from pydantic import BaseModel, Field
from datetime import datetime


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_done: bool | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True