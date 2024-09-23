from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
DB_URL = f"mysql+pymysql://{db_username}:{db_password}@localhost:3306/{db_name}"

engine = create_engine(DB_URL,echo=True,)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()