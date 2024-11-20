import os
import sys

# Add project root to Python path
root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root_dir)
from models.database import Session, BookModel

def get_new_books():
    # Get all PDF files from pdf directory
    root_dir = os.path.dirname(os.path.dirname(__file__))
    pdf_dir = os.path.join(root_dir, "pdfs")
    pdf_files = [f[:-4] for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    
    # Get all books from database
    session = Session()
    db_books = [book.title for book in session.query(BookModel).all()]
    session.close()
    
    # Find books in pdf_files that are not in db_books
    new_books = [title for title in pdf_files if title not in db_books]
    missing_books = [title for title in db_books if title not in pdf_files]
    
    return new_books, missing_books


print(get_new_books())