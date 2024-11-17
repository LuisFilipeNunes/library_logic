from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    
    email = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    booklist = Column(String, default='')  # Comma separated hex codes
    
class BookModel(Base):
    __tablename__ = 'books'
    
    code = Column(String(6), primary_key=True)
    title = Column(String, nullable=False)
    path = Column(String, nullable=False)
    value = Column(Float, nullable=False)

# Create database and tables
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)
