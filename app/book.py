from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    name:str
    auteur:str
    genre:str
    resume:str
    img:str
    dispo: Optional[bool] = True