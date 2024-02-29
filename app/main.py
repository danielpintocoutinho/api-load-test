from fastapi import FastAPI

from .routers import data
from .config import config
from .database import connector

app = FastAPI()
app.include_router(data.router)