# from models.todo_model import TodoModel

# todos = []
# counter = 1


# def create_todo(title: str):
#     global counter
#     todo = TodoModel(counter, title)
#     todos.append(todo)
#     counter += 1
#     return todo


# def get_all():
#     return todos

from sqlalchemy.orm import Session
from models.todo_model import Todo
from datetime import datetime


def create_todo(db: Session, title: str, description: str | None):

    todo = Todo(
        title=title,
        description=description
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_todos(db: Session, limit: int, offset: int):

    return db.query(Todo).offset(offset).limit(limit).all()


def get_total(db: Session):

    return db.query(Todo).count()


def get_todo(db: Session, todo_id: int):

    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo, data: dict):

    for key, value in data.items():
        setattr(todo, key, value)

    todo.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(todo)

    return todo