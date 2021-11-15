from flask import current_app
from datetime import datetime, timezone

from .import db, login_manager
from flask_login import UserMixin

# decorator: to reload the user from user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# The extension will expect certain to have certain attributes and methodes
# is_authenticated, is_active, is_anonymouse get_id we can do manullay but 
#we will import class User Mixin will do all these things for us
     



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

# User Database
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    admin=db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    posts = db.relationship('Update', backref='author', lazy=True)
  

    def __init__(self, name, username, email, password, confirmed, admin=False,
                  confirmed_on=None, image_file=None,):
        self.name=name
        self.username=username          
        self.email = email
        self.registered_on=datetime.now(timezone.utc)
        self.password = password
        self.admin=admin
        self.image_file=image_file
        
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return f"User('{self.name}',{self.username}', '{self.email}')"   

 


# News and updates database

class Update(db.Model):
    __tablename__ = 'updates'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def __init__(self, title, content):
        self.title=title
        self.content=content
        self.date_posted=datetime.now(timezone.utc)

    def __repr__(self):
        return f"Update('{self.title}',{self.content}', '{self.date_posted}')"           

# Upload Database


