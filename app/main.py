from fastapi import FastAPI
from app.api.routes import users, projects, tasks

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])