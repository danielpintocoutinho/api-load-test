from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

SQLALCHEMY_DATABASE_URL = f"postgresql://{config["DB_USER"]}:{
    config["DB_PASS"]}@{config["DB_HOST"]}:{config["DB_PORT"]}/{config["DB_NAME"]}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()