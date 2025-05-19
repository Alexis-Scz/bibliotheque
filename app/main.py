from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas , crud
# models.Base.metadata.drop_all(bind=engine)
# creer la table avec les colonnes
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="l'API d'alexis 🧑",
    description="une api simple pour gerer une biblioteque",
    version="0.0.1"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", description="avoir la liste de tous les livres", response_model=list[schemas.BookOut])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books", description="creer un livre", response_model=schemas.BookOut)
def add_books(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.delete("/books/{id}", description="supprimer un livre avec son id")
def del_books(id:int, db: Session = Depends(get_db)):
    if crud.del_book(db, id):
        return {"message": "book delete"}
    raise HTTPException(status_code=404, detail="livre non trouve")

@app.get("/books/search/{key}", description="avoir les livres qui correspondent au mot clé",response_model=list[schemas.BookOut])
def find_books(key:str,db:Session=Depends(get_db)):
    return crud.find_books(db,key)

@app.put("/books/emprunter/{title}", description="remettre le status dispo a false")
def emprunter_books(title:str,db:Session=Depends(get_db)):
    crud.borrow_books(db, title)
    return {"message":"emprunté ok"}

@app.put("/books/return/{title}", description="remettre le status dispo a true ")
def return_books(title:str,db:Session=Depends(get_db)):
    crud.return_books(db, title)
    return{"message":"retourné ok"}