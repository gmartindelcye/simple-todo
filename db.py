from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

class DBContext:
    def __init__(self):
        self.db = sessionLocal()
    
    def __enter__(self):
        return self.db
    
    def __exit__(self, et, ev, traceback):
        self.db.close()

