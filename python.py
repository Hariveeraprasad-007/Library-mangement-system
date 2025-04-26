class Book:
    def __init__(self,author,title,copies):
        self.title=title
        self.author=author
        self.copies=copies
    @property
    def is_available(self):
        return self.copies>0
    def __str__(self):
        status='Available' if self.is_available else 'Not Available'
        return f'{self.title} by {self.author} is {status}'
class Library:
    def __init__(self):
        self.books=[]
    def add_books(self,book):
        self.books.append(book)
    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                print(book)
    def borrow_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                if book.is_available:
                    book.copies-=1
                    print(f"you have successfully borrowed {title}")
                    print(f"{book.copies} is left")
                else:
                    print(f"{title} is not available")
    def return_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                book.copies+=1
                print(f"{title} is returned")
                print(f"Total copies: {book.copies}")
                return
            else:
                print(f"{title} is not borrowed")
                return
    def search_book_by_author(self,author):
        found=False
        for book in self.books:
            if book.author.lower()==author.lower():
                print(book)
                found=True
        if not found:
            print("no book found on the name of the author")
    def search_book_by_title(self,title):
        found=False
        for book in self.books:
            if book.title==title:
                print(book)
                found=True
        if not found:
            print("Book is not found")

library=Library()
library.add_books(Book('SS Rajamouli','RRR',10))
library.add_books(Book('Sukumar','Puspha',10))
library.add_books(Book('Prashanth Neel','Salaar',10))
library.display_books()
library.borrow_book('RRR')
library.return_book('RRR')
library.return_book('Puspha')
library.search_book_by_author('SS Rajamouli')
library.search_book_by_title('Puspha')
