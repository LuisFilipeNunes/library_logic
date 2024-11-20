import bookstand
import book
class UserBookstand(bookstand.BookStand):
    def __init__(self):
        super().__init__()
        self.user_id = None
    
    def set_user_id(self, user_id):
        self.user_id = user_id

    def add_book(self, book):
        return super().add_book(book)
    
    def get_user_id(self):
        return self.user_id
    
    def __self__(self, verbose = False):    
        if verbose:
            return f"This is the bookstand of the user {self.user_id}, which contains {len(self.books)} books"
                
        identification = {
            'id': self.id,
            'books': len(self.books),
        }
        return identification