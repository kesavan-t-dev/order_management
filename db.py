<<<<<<< HEAD
# db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

USERNAME = "Mssql_db"
PASSWORD = "2025"
SERVERNAME = "localhost"
DBNAME = "orders"
PORT = 52131

connection_url = (
    f"mssql+pymssql://{USERNAME}:{PASSWORD}@{SERVERNAME}:{PORT}/{DBNAME}"
)

engine = create_engine(connection_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


=======
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
>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531

Base = declarative_base()

<<<<<<< HEAD
=======
#Create Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

>>>>>>> 2f7dfd5181a2bf7caa0f5e12869897cff7290531
