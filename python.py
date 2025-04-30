class Book:
    def __init__(self,author,title,copies):
        self.title=title
        self.author=author
        self.copies=copies
        self.reservations={}
    @property
    def is_available(self):
        return self.copies>0
    def __str__(self):
        status='Available' if self.is_available else 'Not Available'
        return f'{self.title} by {self.author} is {status}'
class Library:
    def __init__(self):
        self.books=[]
        self.borrow_books=[]
    def add_books(self,book):
        self.books.append(book)
    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                print(book)
    def borrow_book(self,title,user):
        found=False
        for book in self.books:
            if book.title.lower()==title.lower():
                if book.is_available:
                    book.copies-=1
                    print(f"you have successfully borrowed {title}")
                    print(f"{book.copies} is left")
                    self.borrow_books.append(book)
                    user.borrow_books.append(book)
                    found=True
        if not found:
            print("the book is not found in library")
    def return_book(self,title,user):
        for book in self.books:
            if book.title.lower()==title.lower():
                book.copies+=1
                print(f"{title} is returned")
                print(f"Total copies: {book.copies}")
                self.borrow_books.remove(book)
                user.borrow_books.remove(book)
            else:
                print(f"{title} is not borrowed")
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
            if book.title.lower()==title.lower():
                print(book)
                found=True
        if not found:
            print("Book is not found")
    def display_Not_return_books(self):
        found=False
        print("borrowed books are:")
        for book in self.borrow_books:
            print(book)
            found=True
        if not found:
            print("no books are borrowed")
    def reserve_book(self, title, user):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                if not book.is_available:
                    if user.username not in book.reservations:
                        book.reservations[user.username] = title
                        print(f"{title} is reserved by {user.username}")
                    else:
                        print(f"{title} is already reserved by {user.username}")
                else:
                    print("The book is available; you can borrow it")
        if not found:
            print("There is no book in the library with that title")

    def reserved_books(self):
        for book in self.books:
            for user, title in book.reservations.items():
                print(f"{user}: {title}")
class   User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.borrow_books=[]
    def display_user_books(self):
        print("Borrowed Books: ")
        for book in self.borrow_books:
            print(book)
class Usermanager:
    def __init__(self):
        self.users={}
    def register(self,username,passowrd):
        if username in self.users:
            print("The username exists")
        else:
            self.users[username]=User(username,passowrd)
    def login(self,username,passowrd):
        if username in self.users and self.users[username].password==passowrd:
            print("you have logged successfully")
            return self.users[username]
        else:
            print("Invalid username or password.check it whether you have registered or not")
def main():
    library = Library()
    user_manager = UserManager()

    print("Welcome to the Library System")
    current_user = None

    while not current_user:
        choice = input("Do you want to (1) Register or (2) Login? ")
        if choice == "1":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            user_manager.register(uname, pwd)
        elif choice == "2":
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            current_user = user_manager.login(uname, pwd)

    while True:
        print("\n1-Add Books\n2-Display Books\n3-Borrow Book\n4-Return Book\n5-Search by Author\n6-Search by Title\n7-Display Not Returned Books\n8-Reserve Book\n9-View Reserved Books\n10-My Books\n11-Exit")
        try:
            a = int(input("Enter your choice: "))
            if a == 1:
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Copies: "))
                library.add_books(Book(author, title, copies))
            elif a == 2:
                library.display_books()
            elif a == 3:
                title = input("Enter book title: ")
                library.borrow_book(title, current_user)
            elif a == 4:
                title = input("Enter book title: ")
                library.return_book(title, current_user)
            elif a == 5:
                author = input("Enter author name: ")
                library.search_book_by_author(author)
            elif a == 6:
                title = input("Enter book title: ")
                library.search_book_by_title(title)
            elif a == 7:
                library.display_Not_return_books()
            elif a == 8:
                title = input("Enter book title: ")
                library.reserve_book(title, current_user)
            elif a == 9:
                library.reserved_books()
            elif a == 10:
                current_user.display_user_books()
            elif a == 11:
                print("Exiting... Goodbye!")
                break
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Invalid input")

main()
