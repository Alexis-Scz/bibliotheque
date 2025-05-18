from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    name:str
    auteur:str
    genre:str
    resume:str
    img:str
    dispo: Optional[bool] = True

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True