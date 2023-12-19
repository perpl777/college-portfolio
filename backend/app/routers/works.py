from fastapi import (
    APIRouter, 
    HTTPException, 
    status, 
    Depends)

from ..config.db import get_db
from ..models import Works as WorksModel
from ..models import Authors as AuthorsModel
from ..models import Types as TypesModel
from ..models import Works_Types as Works_TypesModel

from ..schemas import BaseWork, Work

from sqlalchemy.orm import Session

from typing import List


router = APIRouter(
    prefix="/api/works",
    tags=["Works"]
)

@router.get("/", response_description="List of all works", response_model=List[Work], status_code=status.HTTP_200_OK)
def get_all_works(db: Session=Depends(get_db)):
    works = db.query(WorksModel).all()

    if works == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nothign found"
        )

    return works

@router.post("/", response_description="Create new work", response_model=Work, status_code=status.HTTP_201_CREATED)
def create_work(work: BaseWork, db: Session=Depends(get_db)):
    new_work = WorksModel(**work.model_dump())

    db.add(new_work)

    db.commit()

    db.refresh(new_work)

    return new_work

