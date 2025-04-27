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
        self.borrow_books=[]
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
                    self.borrow_books.append(book)
                else:
                    print(f"{title} is not available")
    def return_book(self,title):
        for book in self.books:
            if book.title.lower()==title.lower():
                book.copies+=1
                print(f"{title} is returned")
                print(f"Total copies: {book.copies}")
                self.borrow_books.remove(book)
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
        if username in self.user:
            print("The username exists")
        else:
            self.users[username]=User(username,passowrd)
    def login(self,username,passowrd):
        if username in self.users and self.users[username].password==passowrd:
            print("you have logged successfully")
        else:
            print("Invalid username or password.check it whether you have registered or not")
def main():
    print("1-Add Books")
    print("2-Display Books")
    print("3-Borrow Book")
    print("4-Return Book")
    print("5-Search book by author")
    print("6-Search book by title")
    print("7-Display Not return books")
    print("8-Exit")
    library=Library()
    while True:
        try:
            a=int(input("Enter a correct number(1-8): "))
            if a==1:
                title=input("Enter the title of the book: ")
                author=input("Enter the author of the book: ")
                try:
                    copies=int(input("Enter number of copies are there: "))
                    library.add_books(Book(author,title,copies))
                except ValueError:
                    print("enter the vaaild input for no of copies")
            elif a==2:
                library.display_books()
            elif a==3:
                title=input("enter the title of the book: ")
                library.borrow_book(title)
            elif a==4:
                title=input("enter the title of the book: ")
                library.return_book(title)
            elif a==5:
                author=input("enter the author of the book: ")
                library.search_book_by_author(author)
            elif a==6:
                title=input("enter the title of book: ")
                library.search_book_by_title(title)
            elif a==7:
                library.display_Not_return_books()
            elif a==8:
                break
            else:
                print("enter the correct choice")
        except ValueError:
            print("Enter the valid input for picking choices")
main()
