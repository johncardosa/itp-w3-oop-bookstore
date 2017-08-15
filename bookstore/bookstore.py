class Bookstore(object):
    def __init__(self,name):
        self.name = name
        self.books = []
        self.authors = []
    def get_books(self):
        return self.books
    def add_book(self,book):
        self.books.append(book)
    def search_books(self,author=None,title=None):
        results = []
        for book in self.books:
            if author == book.author or (title and title.lower() in book.title.lower()):
                results.append(book)
        return results

class Author(object):
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    def get_books(self):
        return self.books

class Book(object):
    def __init__(self,title,author):
        self.title = title
        self.author = author
        author.books.append(self)
        
store = Bookstore("Rmotr's bookstore")
borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)

