from fastapi import FastAPI
from routers.todo_router import router as todo_router

app = FastAPI()

app.include_router(todo_router)


@app.get("/health")
def health():
    return {"status": "ok"}