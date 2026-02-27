from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

name = os.getenv("DB_USER", "World")
print(name)


# #DB Connection

# SQLALCHEMY_DATABASE_URL ="postgresql://postgres:35@localhost:5432/blog"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# #Create Session

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

