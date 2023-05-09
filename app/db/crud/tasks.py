from sqlalchemy.orm import Session
from app.db.models import Task
from app.db.schemas import tasks as task_schemas

def create_task(db: Session, task: task_schemas.TaskCreate, project_id: int) -> Task:
    db_task = Task(title=task.title, description=task.description, project_id=project_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task