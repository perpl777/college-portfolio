from pydantic import BaseModel
from typing import Optional

class BaseAuthor(BaseModel):
    name: str
    login: str
    password: str
    email: str
    photo: str

class Author(BaseAuthor):
    id: int