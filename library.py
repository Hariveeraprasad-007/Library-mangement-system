from user import User
from usermanager import UserManager
from datetime import datetime,timedelta
class Library:
    def __init__(self):
        self.users={}
        self.books=[]
        self.borrowed_books=[]
    def add_books(self, book):
        self.books.append(book)
    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                print(book)
    def search_book_by_author(self, author):
        found = False
        for book in self.books:
            if book.author.lower() == author.lower():
                print(book)
                found = True
        if not found:
            print("No book found by that author")
    def search_book_by_title(self, title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
                found = True
        if not found:
            print("Book not found")
    def display_not_returned_books(self):
        if not User.borrow_books:
            print("No books are currently borrowed")
        else:
            print("Borrowed books are:")
            for book in User.borrow_books:
                print(book)
    def reserve_book(self, title, user):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                if not book.is_available:
                    if UserManager.username not in book.reservations:
                        book.reservations[user.username] = title
                        print(f"'{title}' has been reserved by {user.username}")
                    else:
                        print(f"'{title}' is already reserved by {user.username}")
                else:
                    print("The book is available; you can borrow it")
                break
        if not found:
            print("There is no book in the library with that title")
    def reserved_books(self):
        for book in self.books:
            for user, title in book.reservations.items():
                print(f"{user}: {title}")
    def calculate_fine(self,user,title):
        fined=False
        found=False
        for record in user.borrow_books_record:
            if record['title'].lower()==title.lower():
                found=True
                current_date=datetime.now()
                due_date=record['due_date']
                if current_date>due_date:
                    overdue_days=(current_date-due_date).days
                    fine=overdue_days*10
                    print(f"Book '{title}' is overdue by {days_overdue} days. Fine: ₹{fine}")
                    fined=True
        if not found:
            print("the title you enterd is not in the borrowed books")
        if not fined:
            return 0
        return fine
