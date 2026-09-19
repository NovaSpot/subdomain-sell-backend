import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

"""

psycopg2 is the most popular PostgreSQL database adapter for the 
Python programming language. it support async, and has a stable codebase.
alternative are:
    - asyncpg
    - aiopg

in relational dbs, we dont create tables for each users as it is 
memory intensive and not scalable. instead we create a single table.

we should need tables like:
    - users
    - profiles
    - domains
    

note that these are plural, as we will have multiple users and profiles. 


"""


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
