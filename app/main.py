from fastapi import FastAPI
from app.db.base import Base, engine
from app.api.routes import users, projects, tasks

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Task Manager API!"}