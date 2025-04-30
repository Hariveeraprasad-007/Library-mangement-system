from library import Library
from datetime import datetime,timedelta
class User:
    def __init__(self):
        self.borrow_books_record=[]
    def display_user_books(self):
        if not self.borrow_books_record:
            print("No books borrowed.")
        else:
            print("Borrowed Books:")
            for record in self.borrow_books_record:
                print(f"Title: {record['title']} | Borrowed on: {record['borrow_date'].date()} | Due by: {record['due_date'].date()}")
    def return_book(self, title, user):
        found = False
        for book in self.borrow_books_record:
            if book['title'].lower() == title.lower():
                for Book in Library.books:
                    Book.copies += 1
                    print(f"'{title}' has been returned")
                    print(f"Total copies: {Book.copies}")
                    found=True
                self.borrow_books_record.remove(book)
                Library.borrowed_books.remove(book)
        if not found:
            print(f"'{title}' was not borrowed")
    def borrow_book(self, title, user):
        found = False
        for book in Library.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    borrow_date=datetime.now()
                    due_date=borrow_date+timedelta(days=14)
                    book.copies -= 1
                    print(f"You have successfully borrowed {title} at time {borrow_date} and due date for this book is {due_date}")
                    print(f"{book.copies} copies left")
                    self.borrow_books_record.append({'title':title,'borrow date':borrow_date,'due_date':due_date})
                    Library.borrowed_books.append(book)
                    found = True
                    break
        if not found:
            print("The book is not found in the library")