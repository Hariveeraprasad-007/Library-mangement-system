
class Book:
    def __init__(self, author, title, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.reservations = {}
    @property
    def is_available(self):
        return self.copies > 0
    def __str__(self):
        status = 'Available' if self.is_available else 'Not Available'
        return f'{self.title} by {self.author} is {status}'