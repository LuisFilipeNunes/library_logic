import bookstand
from book import Book
from managers_utils.code_generator import generate_unique_code
from managers_utils.cover_manager import create_book_cover

class LibraryBookstand(bookstand.BookStand):
    def __init__(self):
        super().__init__()
        
    def add_book(self, title):
        ''' 
            This method will construct a book object and add it to the bookstand.
            The first step is to check if the book is already in the bookstand, secondly, if aint, then it will make a coverpage. With a coverpage done, it will generate a new code for it. 
            Finally, it will add the book to the bookstand.
        '''
        for single_title in [title] if isinstance(title, str) else title:
            for book in self.books:
                if book.title == single_title:
                    print(f"Book '{single_title}' already in the bookstand.")
                    continue
            
            coverpage = create_book_cover(single_title)
            code = generate_unique_code()
            pdf_path = f"bookstand/pdf/{single_title}.pdf"
            self.books.append(Book(title=single_title, book_code=code, path=pdf_path, coverpage=coverpage))
