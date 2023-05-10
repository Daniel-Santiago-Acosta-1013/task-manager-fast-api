from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.crud import projects as project_crud
from app.db.schemas import projects as project_schemas, users as user_schemas
from app.api.dependencies import get_current_user
from app.db.session import db_session

router = APIRouter()

@router.post("/", response_model=project_schemas.Project)
async def create_project(project: project_schemas.ProjectCreate, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        new_project = project_crud.create_project(db, project, owner_id=current_user.id)
    return new_project

@router.get("/", response_model=List[project_schemas.Project])
async def get_projects(current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        projects = project_crud.get_projects(db, owner_id=current_user.id)
    return projects

@router.get("/{project_id}", response_model=project_schemas.Project)
async def get_project(project_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        project = project_crud.get_project(db, project_id)
        if project.owner_id != current_user.id:
            raise HTTPException(status_code=400, detail="Not enough permissions")
    return project

@router.put("/{project_id}", response_model=project_schemas.Project)
async def update_project(project_id: int, project: project_schemas.ProjectUpdate, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        updated_project = project_crud.update_project(db, project_id, project)
    return updated_project

@router.delete("/{project_id}", response_model=project_schemas.Project)
async def delete_project(project_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        project = project_crud.delete_project(db, project_id)
    return project
