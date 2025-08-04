from app.model.Feedback import Feedback
from main import db
from sqlalchemy.orm import scoped_session

class Feedback_Repo:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_mail(args, session:scoped_session):
        feedback = Feedback (
            user_email = args['user_email'],
            message = args['message']
        )
        session.add(feedback)
        session.commit()
        return  feedback