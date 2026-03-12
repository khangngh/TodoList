from fastapi import FastAPI
from core.database import Base, engine
from routers.todo_router import router as todo_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo_router)


@app.get("/health")
def health():
    return {"status": "ok"}