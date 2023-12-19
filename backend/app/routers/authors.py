from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config.db import get_db

from ..models import Authors as AuthorsModel

from ..schemas import BaseAuthor, Author

from sqlalchemy.orm import Session

from typing import List


router = APIRouter(
    prefix="/api/authors",
    tags=["Authors"]
)

@router.get("/", response_description="List of all authors", response_model=List[Author], status_code=status.HTTP_200_OK)
def get_all_works(db: Session=Depends(get_db)):
    authors = db.query(AuthorsModel).all()

    if authors == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No authors found"
        )

    return authors

@router.post("/", response_description="Create new author", response_model=Author, status_code=status.HTTP_201_CREATED)
def create_work(author: BaseAuthor, db: Session=Depends(get_db)):
    new_author = AuthorsModel(**author.model_dump())

    db.add(new_author)

    db.commit()

    db.refresh(new_author)

    return new_author

