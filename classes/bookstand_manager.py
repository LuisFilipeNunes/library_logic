from classes.bookstand import Bookstand
from classes.user_bookstand import UserBookstand
from classes.library_bookstand import LibraryBookstand
from classes.book import Book
from typing import List

class BookstandManager():
    def __init__(self):
        self.bookstand: List[UserBookstand] = []
        self.library: LibraryBookstand

    def add_bookstand(self, UserBookstand):
        self.bookstand.append(UserBookstand)
    
    def add_book_to_user(self, user_id, book_code):
        for bookstand in self.bookstand:
            if bookstand.user_id == user_id:
                book = self.library.get_book(book_code)
                if book:
                    bookstand.add_book(book)
                    return True
        return False
    
    def remove_book_from_user(self, user_id, book_code):
        for bookstand in self.bookstand:
            if bookstand.user_id == user_id:
                book = self.library.get_book(book_code)
                if book:
                    bookstand.remove_book(book_code)
                    return True
        return False