from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import router as task_router
from src.user.router import router as users_router

Base.metadata.create_all(engine)

app = FastAPI(
    title="Task Management App",
    version="1.0"
)

app.include_router(task_router)
app.include_router(users_router)

