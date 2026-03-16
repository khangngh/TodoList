from sqlalchemy.orm import Session
from models.todo_model import Todo
from datetime import datetime


def create_todo(db, title, description, owner_id, due_date=None, tags=None):

    todo = Todo(
        title=title,
        description=description,
        owner_id=owner_id,
        due_date=due_date,
        tags=tags
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_todos(db, owner_id, limit, offset):

    return (
        db.query(Todo)
        .filter(Todo.owner_id == owner_id)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_total(db, owner_id):

    return (
        db.query(Todo)
        .filter(Todo.owner_id == owner_id)
        .count()
    )


def get_todo(db: Session, todo_id: int):

    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo, data: dict):

    for key, value in data.items():
        setattr(todo, key, value)
    todo.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(todo)
    return todo


def get_overdue_todos(db: Session, owner_id: int):
    now = datetime.utcnow()
    return (
        db.query(Todo)
        .filter(Todo.owner_id == owner_id, Todo.due_date < now, Todo.is_done == False)
        .all()
    )


def get_today_todos(db: Session, owner_id: int):
    today = datetime.utcnow().date()
    return (
        db.query(Todo)
        .filter(Todo.owner_id == owner_id, Todo.due_date.isnot(None), Todo.is_done == False)
        .filter(Todo.due_date >= datetime(today.year, today.month, today.day),
                Todo.due_date < datetime(today.year, today.month, today.day + 1))
        .all()
    )

    todo.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(todo)

    return todo

def get_todos(db, owner_id, limit, offset):

    return (
        db.query(Todo)
        .filter(Todo.owner_id == owner_id)
        .offset(offset)
        .limit(limit)
        .all()
    )
