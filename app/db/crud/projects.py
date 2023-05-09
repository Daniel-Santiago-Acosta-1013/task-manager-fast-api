from sqlalchemy.orm import Session
from app.db.models import Project
from app.db.schemas import projects as project_schemas

def create_project(db: Session, project: project_schemas.ProjectCreate, user_id: int) -> Project:
    db_project = Project(name=project.name, description=project.description, owner_id=user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project