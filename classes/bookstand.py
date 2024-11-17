from typing import List
from book import Book
class BookStand():
    def __init__(self):
        self.books: List[Book] = []  # List to store Book objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_book(self, book_code):
        for book in self.books:
            if book.get_att('id') == book_code:
                return book