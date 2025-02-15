import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

SQL_DATABASE_URI = os.getenv('SQL_DATABASE_URI')

engine = create_engine(
    SQL_DATABASE_URI,
    pool_size=10,
    max_overflow=20,
    pool_timeout=60
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
