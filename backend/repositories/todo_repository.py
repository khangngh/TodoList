from models.todo_model import TodoModel

todos = []
counter = 1


def create_todo(title: str):
    global counter
    todo = TodoModel(counter, title)
    todos.append(todo)
    counter += 1
    return todo


def get_all():
    return todos