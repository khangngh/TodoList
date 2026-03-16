from repositories.todo_repository import *
from fastapi import HTTPException


def create_new_todo(db, title, description, owner_id):

    return create_todo(db, title, description, owner_id)


def list_todos(db, owner_id, limit, offset):

    items = get_todos(db, owner_id, limit, offset)

    total = get_total(db, owner_id)

    return {
        "items": items,
        "total": total,
        "limit": limit,
        "offset": offset
    }


def patch_todo(db, todo_id, data):

    todo = get_todo(db, todo_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return update_todo(db, todo, data)

def get_todo_by_owner(db, todo_id, owner_id):

    todo = get_todo(db, todo_id)

    if not todo or todo.owner_id != owner_id:
        raise HTTPException(404, "Todo not found")

    return todo