from classes.bookstand import Bookstand
from classes.user_bookstand import UserBookstand
from classes.book import Book
from typing import List

class BookstandManager():
    def __init__(self):
        self.bookstand: List[UserBookstand] = []

    def add_bookstand(self, UserBookstand):
        self.bookstand.append(UserBookstand)
    
    