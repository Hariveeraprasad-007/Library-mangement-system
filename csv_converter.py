
import csv
from datetime import datetime
def save_books_to_csv(books, filename='books.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'author', 'copies'])
        for book in books:
            writer.writerow([book.title, book.author, book.copies])
def load_books_from_csv(filename='books.csv'):
    from book import Book
    books = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(Book(row['author'], row['title'], int(row['copies'])))
    except FileNotFoundError:
        pass
    return books
def save_users_to_csv(users, filename='users.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password'])
        for user in users.values():
            writer.writerow([user.username, user.password])
def load_users_from_csv(filename='users.csv'):
    from user import User
    users = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row['username']] = User(row['username'], row['password'])
    except FileNotFoundError:
        pass
    return users
def save_borrowed_to_csv(users, filename='borrowed.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'title', 'borrow_date', 'due_date'])
        for user in users.values():
            for record in user.borrowed_books_records:
                writer.writerow([
                    user.username,
                    record['title'],
                    record['borrow_date'].strftime('%Y-%m-%d'),
                    record['due_date'].strftime('%Y-%m-%d')
                ])
def load_borrowed_from_csv(users, filename='borrowed.csv'):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                username = row['username']
                if username in users:
                    users[username].borrowed_books_records.append({
                        'title': row['title'],
                        'borrow_date': datetime.strptime(row['borrow_date'], '%Y-%m-%d'),
                        'due_date': datetime.strptime(row['due_date'], '%Y-%m-%d')
                    })
    except FileNotFoundError:
        pass