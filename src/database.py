import os 
from sqlmodel import SQLModel, Session 
from sqlalchemy import create_engine 

from dotenv import load_dotenv
load_dotenv() 


## RDS MYSQL OPS    
  
DATABASE_USER = os.environ['RDS_USER']
DATABASE_PASSWORD = os.environ['RDS_PASSWORD']
DATABASE_HOST = os.environ['RDS_HOST']
DATABASE_PORT = os.environ['RDS_PORT']
DATABASE_NAME = os.environ['RDS_DB_NAME']

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
#DATABASE_URL= "mysql+pymysql://mlops_user:Ankara06@localhost:3306/mlops"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
 