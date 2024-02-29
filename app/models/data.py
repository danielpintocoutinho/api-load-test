from sqlalchemy import Column, Integer, String
from app.database import Base

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    message = Column(String, index=True)
