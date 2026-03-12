from repositories.todo_repository import *
from fastapi import HTTPException


def create_new_todo(db, title, description):

    return create_todo(db, title, description)


def list_todos(db, limit, offset):

    items = get_todos(db, limit, offset)

    total = get_total(db)

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