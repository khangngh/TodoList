# from repositories.todo_repository import get_all, create_todo


# def create_new_todo(title):
#     todo = create_todo(title)
#     return todo.to_dict()

# def list_todos(is_done=None, q=None, sort=None, limit=10, offset=0):

#     todos = get_all()

#     # filter
#     if is_done is not None:
#         todos = [t for t in todos if t.is_done == is_done]

#     # search
#     if q:
#         todos = [t for t in todos if q.lower() in t.title.lower()]

#     # sort
#     if sort == "created_at":
#         todos = sorted(todos, key=lambda x: x.created_at)

#     if sort == "-created_at":
#         todos = sorted(todos, key=lambda x: x.created_at, reverse=True)

#     total = len(todos)

#     todos = todos[offset: offset + limit]

#     return {
#         "items": [t.to_dict() for t in todos],
#         "total": total,
#         "limit": limit,
#         "offset": offset
#     }

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