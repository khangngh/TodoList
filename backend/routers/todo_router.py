from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.todo_schema import *
from services.todo_service import *
from core.dependencies import get_current_user
from models.user_model import User



router = APIRouter(prefix="/api/v1/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse)
def create(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_new_todo(
        db,
        todo.title,
        todo.description,
        current_user.id
    )


@router.get("/")
def get_all(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return list_todos(db, current_user.id, limit, offset)

@router.patch("/{todo_id}", response_model=TodoResponse)
def update(todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)):

    return patch_todo(db, todo_id, data.dict(exclude_unset=True))

@router.post("/")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_new_todo(
        db,
        title=todo.title,
        description=todo.description,
        owner_id=current_user.id
    )