from models.database import Session, UserModel
import random

def generate_user_id():
    session = Session()
    while True:
        # Generate a 5-digit number with leading zeros
        new_id = f"{random.randint(0, 99999):05d}"
        
        # Check if ID exists in database
        user_exists = session.query(UserModel).filter_by(id=new_id).first()
        
        if not user_exists:
            session.close()
            return new_id
