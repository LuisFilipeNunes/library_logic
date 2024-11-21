from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
# Create data directory if it doesn't exist
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(String(5), nullable=False)
    email = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    booklist = Column(String, default='')  # Comma separated hex codes
    
class BookModel(Base):
    __tablename__ = 'books'
    
    code = Column(String(6), primary_key=True)
    title = Column(String, nullable=False)
    path = Column(String, nullable=False)
    cover = Column(String, nullable=False)
    value = Column(Float, nullable=False)

# Updated engine with new path
engine = create_engine(f'sqlite:///{os.path.join(data_dir, "library.db")}')
Base.metadata.create_all(engine)

# Session factory remains the same
Session = sessionmaker(bind=engine)
