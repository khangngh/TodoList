from fastapi import FastAPI
from core.database import Base, engine
from routers.todo_router import router as todo_router
from routers.auth_router import router as auth_router

# QUAN TRỌNG
from models.user_model import User
from models.todo_model import Todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo_router)
app.include_router(auth_router)


@app.get("/health")
def health():
    return {"status": "ok"}