from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.crud import tasks as task_crud
from app.db.schemas import tasks as task_schemas, users as user_schemas
from app.api.dependencies import get_current_user
from app.db.session import db_session

router = APIRouter()

@router.post("/", response_model=task_schemas.Task)
async def create_task(task: task_schemas.TaskCreate, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        new_task = task_crud.create_task(db, task, owner_id=current_user.id)
    return new_task

@router.get("/", response_model=List[task_schemas.Task])
async def get_tasks(current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        tasks = task_crud.get_tasks(db, owner_id=current_user.id)
    return tasks

@router.get("/{task_id}", response_model=task_schemas.Task)
async def get_task(task_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        task = task_crud.get_task(db, task_id)
        if task.owner_id != current_user.id:
            raise HTTPException(status_code=400, detail="Not enough permissions")
    return task

@router.put("/{task_id}", response_model=task_schemas.Task)
async def update_task(task_id: int, task: task_schemas.TaskUpdate, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        updated_task = task_crud.update_task(db, task_id, task)
    return updated_task

@router.delete("/{task_id}", response_model=task_schemas.Task)
async def delete_task(task_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        task = task_crud.delete_task(db, task_id)
    return task

@router.post("/{task_id}/assign/{user_id}", response_model=task_schemas.Task)
async def assign_task(task_id: int, user_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        task = task_crud.assign_task(db, task_id, user_id)
    return task
