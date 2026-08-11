from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from shared.config.settings import Settings


# Load Cart Service .env
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

settings = Settings()


# Database connection
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


# Database session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# SQLAlchemy Base
Base = declarative_base()


# FastAPI database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()