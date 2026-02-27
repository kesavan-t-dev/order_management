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




