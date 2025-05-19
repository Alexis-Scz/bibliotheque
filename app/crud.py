from sqlalchemy.orm import Session
from sqlalchemy import update
from . import models, schemas

def get_books(db:Session):
    return db.query(models.Book).all()

def create_book (db:Session, book: schemas.BookCreate):
    db_book = models.Book(
        name=book.name,
        auteur=book.auteur,
        genre=book.genre,
        img=book.img,
        resume=book.resume,
        dispo=book.dispo
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def del_book(db: Session, id: int):
    book = db.query(models.Book).get(id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False

def find_books(db:Session,key:str):
    books=db.query(models.Book).all()
    key = key.lower()
    return [book for book in books if key in book.name.lower() or key in book.auteur.lower() or key in book.genre.lower() ]

def borrow_books(db:Session,title:str):
    db.query(models.Book).filter(models.Book.name==title).update({"dispo":False})
    db.commit()


def return_books(db:Session,title:str):
    db.query(models.Book).filter(models.Book.name==title).update({"dispo":True})
    db.commit()