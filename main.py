from book import Book
from library import Library
from usermanager import UserManager
from user import User
from csv_converter import (
    save_books_to_csv, load_books_from_csv,
    save_users_to_csv, load_users_from_csv,
    save_borrowed_to_csv, load_borrowed_from_csv
)
def main():
    library = Library()
    library.books = load_books_from_csv()
    user_manager = UserManager("admin", "admin")
    user_manager.users = load_users_from_csv()
    load_borrowed_from_csv(user_manager.users)
    current_user = None
    while True:
        print("\nLibrary Management System")
        print("1 - Register")
        print("2 - Login")
        print("3 - Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_manager.login(username, password)
            if user:
                current_user = user
                while True:
                    print("\nLibrary Operations")
                    print("1 - Add Book (Librarian)")
                    print("2 - Display Books")
                    print("3 - Borrow Book")
                    print("4 - Return Book")
                    print("5 - Search Book by Author")
                    print("6 - Search Book by Title")
                    print("7 - Display Not Returned Books")
                    print("8 - Reserve Book")
                    print("9 - Calculate Fine")
                    print("10 - Show My Borrowed Books")
                    print("11 - Logout")
                    operation = input("Enter operation number: ")
                    if operation == '1':
                        if current_user.username == "admin":
                            title = input("Enter book title: ")
                            author = input("Enter book author: ")
                            copies = int(input("Enter number of copies: "))
                            book = Book(author, title, copies)
                            library.add_books(book)
                            save_books_to_csv(library.books)
                            print("Book added successfully.")
                        else:
                            print("Only librarian (admin) can add books.")
                    elif operation == '2':
                        library.display_books()
                    elif operation == '3':
                        title = input("Enter the title of the book to borrow: ")
                        current_user.borrow_book(title, current_user)
                        save_borrowed_to_csv(user_manager.users)
                    elif operation == '4':
                        title = input("Enter the title of the book to return: ")
                        current_user.return_book(title, current_user)
                        save_books_to_csv(library.books)
                    elif operation == '5':
                        author = input("Enter the author to search for: ")
                        library.search_book_by_author(author)
                    elif operation == '6':
                        title = input("Enter the title to search for: ")
                        library.search_book_by_title(title)
                    elif operation == '7':
                        library.display_not_returned_books()
                    elif operation == '8':
                        title = input("Enter the title of the book to reserve: ")
                        library.reserve_book(title, current_user)
                    elif operation == '9':
                        title = input("Enter the title of the book to calculate fine: ")
                        library.calculate_fine(current_user, title)
                    elif operation == '10':
                        current_user.display_user_books()
                    elif operation == '11':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid operation. Please enter a number between 1 and 11.")
        elif choice == '3':
            save_books_to_csv(library.books)
            save_users_to_csv(user_manager.users)
            save_borrowed_to_csv(user_manager.users)
            print("Data saved. Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()