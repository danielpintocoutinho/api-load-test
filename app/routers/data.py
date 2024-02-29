from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from time import time

from app.controllers import data as controller
from app.database.connector import engine
from app.dependencies import get_db
from app.models.data import Base, Data as DataModel
from app.schemas.data import Data as DataSchema, DataList as DataListSchema


Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/data",
    tags=["data"],
)


@router.get("", response_model=DataListSchema)
async def read_data(limit: int = 100, db: Session = Depends(get_db)):
    start = time()
    data_list = controller.get_data(db, limit)
    end = time()

    return {'data': data_list, 'time': end - start}


@router.get("/{id}", response_model=DataSchema)
async def read_data_by_id(id: int, db: Session = Depends(get_db)):
    start = time()
    current_data = controller.get_data_by_id(db, data_id=id)
    end = time()

    if current_data is None:
        raise HTTPException(status_code=404, detail="Data not found")

    setattr(current_data, 'time', end - start)
    return current_data