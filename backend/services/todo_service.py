from repositories.todo_repository import get_all, create_todo


def create_new_todo(title):
    todo = create_todo(title)
    return todo.to_dict()

def list_todos(is_done=None, q=None, sort=None, limit=10, offset=0):

    todos = get_all()

    # filter
    if is_done is not None:
        todos = [t for t in todos if t.is_done == is_done]

    # search
    if q:
        todos = [t for t in todos if q.lower() in t.title.lower()]

    # sort
    if sort == "created_at":
        todos = sorted(todos, key=lambda x: x.created_at)

    if sort == "-created_at":
        todos = sorted(todos, key=lambda x: x.created_at, reverse=True)

    total = len(todos)

    todos = todos[offset: offset + limit]

    return {
        "items": [t.to_dict() for t in todos],
        "total": total,
        "limit": limit,
        "offset": offset
    }