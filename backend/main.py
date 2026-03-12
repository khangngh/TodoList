from fastapi import FastAPI, HTTPException
from schemas import Todo
from models import TodoModel

app = FastAPI()

todos = []


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Welcome to ToDo API"}


@app.post("/todos")
def create_todo(todo: Todo):
    new_todo = TodoModel(todo.id, todo.title, todo.is_done)
    todos.append(new_todo)
    return new_todo.to_dict()


@app.get("/todos")
def get_todos():
    return [todo.to_dict() for todo in todos]


@app.get("/todos/{id}")
def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo.to_dict()
    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{id}")
def update_todo(id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = TodoModel(updated_todo.id, updated_todo.title, updated_todo.is_done)
            return todos[index].to_dict()
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{id}")
def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            deleted = todos.pop(index)
            return deleted.to_dict()
    raise HTTPException(status_code=404, detail="Todo not found")