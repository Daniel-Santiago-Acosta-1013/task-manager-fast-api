from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.crud import users as user_crud
from app.db.schemas import users as user_schemas
from app.api.dependencies import get_current_user
from app.db.session import db_session
from app.core.security import create_access_token

router = APIRouter()

@router.post("/", response_model=user_schemas.User)
async def create_user(user: user_schemas.UserCreate):
    with db_session() as db:
        new_user = user_crud.create_user(db, user)
    return new_user

@router.post("/login", response_model=user_schemas.Token)
async def login(user: user_schemas.UserLogin):
    with db_session() as db:
        db_user = user_crud.authenticate_user(db, user.email, user.password)
        if not db_user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        access_token = create_access_token(data={"sub": db_user.email})
        return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=user_schemas.User)
async def get_me(current_user: user_schemas.User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=user_schemas.User)
async def update_me(user: user_schemas.UserUpdate, current_user: user_schemas.User = Depends(get_current_user)):
    with db_session() as db:
        updated_user = user_crud.update_user(db, current_user.id, user)
    return updated_user