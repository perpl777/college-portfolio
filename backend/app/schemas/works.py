from pydantic import BaseModel
from typing import Optional
from datetime import date

class BaseWork(BaseModel):
    date: date
    title: str
    description: str
    image: str
    author: int

class Work(BaseWork):
    id: int