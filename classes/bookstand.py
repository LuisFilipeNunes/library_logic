from typing import List
from classes.book import Book
class BookStand():
    def __init__(self):
        self.books: List[Book] = []  # List to store Book objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def get_book(self, identifier):
        for book in self.books:
            if book.get_att('id') == identifier or book.get_att('title') == identifier:
                return book
            
    def remove_book(self, identifier):
        for book in self.books:
            if book.get_att('id') == identifier or book.title == identifier:
                self.books.remove(book)
                return True
        return False
