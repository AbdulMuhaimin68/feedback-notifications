from main import db
from datetime import datetime

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    feedback_id = db.Column(db.Integer, primary_key = True)
    user_email = db.Column(db.String(255), nullable = False)
    message = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow())
    