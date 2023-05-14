from sqlalchemy.orm import Session
from app.db.models.users import User  # Cambia aquí
from app.db.schemas.users import UserCreate
from app.core.security import get_password_hash

def create_user(db: Session, user: UserCreate) -> User:  # Cambia aquí
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)  # Cambia aquí
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()  # Cambia aquí