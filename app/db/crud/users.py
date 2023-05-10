from sqlalchemy.orm import Session
from app.db.models import User
from app.db.schemas import users as user_schemas
from app.core.security import get_password_hash

def create_user(db: Session, user: user_schemas.UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user