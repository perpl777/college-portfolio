from sqlalchemy import Column, Integer, String, ForeignKey
from ..config.db import Base
from .works import Works as WorksModel
from .types import Types as TypesModel


class Works_Types(Base):
    __tablename__ = "works_types"

    work_id = Column(
        Integer, 
        ForeignKey(WorksModel.id), 
        nullable=False, 
        primary_key=True
    )
    type_id = Column(
        Integer, 
        ForeignKey(TypesModel.id), 
        nullable=False, 
        primary_key=True
    )