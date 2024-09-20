from pydantic import BaseModel, ValidationError
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from data import models


class Item(BaseModel):
    id: int
    name: str
    title: str
    description: str

ServerEntity = sqlalchemy_to_pydantic(models.Server)

