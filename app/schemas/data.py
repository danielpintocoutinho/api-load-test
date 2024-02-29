from pydantic import BaseModel

class Data(BaseModel):
    id: int
    message: str
    time: float

    class Config:
        from_attributes = True

class DataList(BaseModel):
    data: list[Data]
    time: float

    class Config:
        from_attributes = True