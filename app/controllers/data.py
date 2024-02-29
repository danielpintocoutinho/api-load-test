from sqlalchemy.orm import Session

from app.models.data import Data as DataModel


def get_data(db: Session, limit: int = 100):
    return db.query(DataModel).limit(limit).all()


def get_data_by_id(db: Session, data_id: int):
    return db.query(DataModel).filter(DataModel.id == data_id).first()
