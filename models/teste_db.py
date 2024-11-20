from database import Session, UserModel, BookModel

# Create a session
session = Session()

# Create new user
new_user = UserModel(
    name="John Doe",
    email="john@example.com",
    password="secret123",
    booklist="AABBCC,DDEEFF"
)

# Create new book
new_book = BookModel(
    code="ABC123",
    title="Python Programming",
    cover="/covers/python.png",
    path="/books/python.pdf",
    value=29.99
)

# Add to database
session.add(new_user)
session.add(new_book)
session.commit()
