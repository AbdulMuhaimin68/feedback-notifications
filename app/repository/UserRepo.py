from main import db
from app.model.User import User
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash

class UserRepository:
    
    @staticmethod
    def get_session():
        return db.session()
    
    @staticmethod 
    def add_user(args, session:scoped_session):
        hash_password = generate_password_hash(args['password'])
        user = User(
            # user_id = args['user_id'],
            username = args['username'],
            email = args['email'],
            password = hash_password
        )
        session.add(user)
        session.commit()
        return user
    
    @staticmethod
    def get_through_email(args, session:scoped_session):
        email = args['email']
        user = session.query(User).filter(User.email == email).first()
        return user