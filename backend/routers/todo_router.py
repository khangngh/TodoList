from fastapi import APIRouter, Query
from schemas.todo_schema import TodoCreate
from services.todo_service import create_new_todo, list_todos

router = APIRouter(prefix="/api/v1/todos", tags=["Todos"])


@router.post("/")
def create(todo: TodoCreate):
    return create_new_todo(todo.title)


@router.get("/")
def get_all(
    is_done: bool | None = None,
    q: str | None = None,
    sort: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    return list_todos(is_done, q, sort, limit, offset)