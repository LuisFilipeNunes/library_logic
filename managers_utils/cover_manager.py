from pdf2image import convert_from_path
import os

def create_book_cover(title):
    # Get the path to the project root directory
    root_dir = os.path.dirname(os.path.dirname(__file__))
    
    pdf_path = os.path.join(root_dir, "pdfs", f"{title}.pdf")
    cover_path = os.path.join(root_dir, "covers", f"cover_{title}.png")
    if not os.path.exists(pdf_path):
        print(f"PDF for '{title}' not found in bookstand.")
        return FileNotFoundError
        
    pages = convert_from_path(pdf_path, first_page=1, last_page=1)
    pages[0].save(cover_path, 'PNG')
    
    return cover_path
