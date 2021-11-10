from app import app
from datetime import datetime
from app import db

# Contact Database Model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    sno = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(200))
    last_name= db.Column(db.String(200))
    email= db.Column(db.String(200))
    feedback = db.Column(db.Text())

    # now we need to define the constructor
    def __init__(self, first_name, last_name, email, feedback):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.feedback=feedback