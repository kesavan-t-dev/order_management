from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()
db_url = os.getenv("url", "Not Found")
print(db_url)


# #DB Connection

SQLALCHEMY_DATABASE_URL = db_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Create Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

