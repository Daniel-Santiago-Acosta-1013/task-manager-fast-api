from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session.
def db_session():
    """Returns a session for the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

# Import all SQLAlchemy models.
from app.db.models import users, projects, tasks  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)
