from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.db.schemas.users import User, TokenData
from app.core.security import verify_password, get_password_hash
from app.db.crud.users import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Implement the logic to get the current user from the token
    # Raise an exception if the token is invalid or the user is not found
    return