from book import Book

class Bibliotheque:
    def __init__(self):
        self.books=[]

# post /books ✅
    def add_book(self, book: Book):
        self.books.append(book)
        
# get  /books ✅
    def get_book(self):
        return self.books
        
# del /books ✅
    def del_book(self, title:str):
        book_len = len(self.books)
        self.books = [book for book in self.books if book.name != title]
        return len(self.books) < book_len
    
# get  /books/search ✅
    def find_book(self, key:str):
        key = key.lower()
        return [
            book for book in self.books
            if key in book.name.lower()
            or key in book.auteur.lower()
            or key in book.genre.lower()
            ]
    
# put /books/emprunter ✅
    def emprunter_book(self, title:str):
        for book in self.books:
            if book.name==title and book.dispo:
                book.dispo=False
                return True
        return False
    
# put /books/return ✅
    def return_book(self, title:str):
        for book in self.books:
            if book.name==title and not book.dispo:
                book.dispo=True
                return True
        return False


 