import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Engine to talk to PostgreSQL
engine = create_engine(DATABASE_URL)

# Session factory for handling requests
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for database models
Base = declarative_base()

# Dependency to provide a database session per web request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
