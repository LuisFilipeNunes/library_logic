import os
import sys

# Add project root to Python path
root_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(root_dir)
from models.database import Session, BookModel
import random
import string

def generate_unique_code():
    session = Session()
    
    while True:
        code = ''.join(random.choices(string.hexdigits, k=6)).upper()
        existing_book = session.query(BookModel).filter(BookModel.code == code).first()
        
        if not existing_book:
            session.close()
            return code

print(generate_unique_code())
