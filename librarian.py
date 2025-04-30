from usermanager import UserManager
from book import Book
class Librarian(UserManager):
    def __init__(self,librarian_name,librarian_password):
        super()__init__(librarian_name,librarian_password)
    def add_books(self,title,author,copies):
        book=Book(title,author,copies)
        print(f"{copies} of {title} by {author} is added")