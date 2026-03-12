from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db

from schemas.todo_schema import *
from services.todo_service import *

router = APIRouter(prefix="/api/v1/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse)
def create(todo: TodoCreate, db: Session = Depends(get_db)):

    return create_new_todo(db, todo.title, todo.description)


@router.get("/")
def get_all(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):

    return list_todos(db, limit, offset)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update(todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)):

    return patch_todo(db, todo_id, data.dict(exclude_unset=True))