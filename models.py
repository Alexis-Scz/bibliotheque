from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    auteur=Column(String)
    genre=Column(String)
    resume=Column(String)
    img=Column(String)
    dispo= Column(Boolean, default=True)