
from flask import current_app
from datetime import datetime, timezone
from flask import redirect, url_for, abort
from flask.helpers import flash
from flask_admin.contrib.sqla.view import ModelView
from flask_admin.model.base import BaseModelView
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .import db, login_manager
from flask_login import UserMixin, current_user



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
    phonenumber=db.Column(db.String(15), unique=True)
    password = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    admin=db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    posts = db.relationship('Update', backref='author', lazy=True)
    image=db.relationship('UploadImg', backref='author', lazy=True)
  

    def __init__(self, name, username, email, phonenumber, password, confirmed, admin=False,
                  confirmed_on=None, image_file=None,):
        self.name=name
        self.username=username          
        self.email = email
        self.phonenumber=phonenumber
        self.registered_on=datetime.now(timezone.utc)
        self.password = password
        self.admin=admin
        self.image_file=image_file
        
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
    
    # Password Reset Token Methode

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod # tell python  not expect token as self argument
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)    

    def __repr__(self):
        return f"{self.name},{self.username}, {self.email}, {self.phonenumber}, {self.image_file}"  


# Authorization admin view we will import this class in __init__.py
class AdminView(ModelView):
    def is_accessible(self):
        if current_user.admin==True:
            return current_user.is_authenticated
        else:    
            return abort(403)
    def handle_view(self):
        if not self.is_accessible():
            flash('you are not authorized', 'info')
            return redirect(url_for('main.home')) 

class UserView(AdminView):
    column_list = ('name', 'username', 'email', 'phonenumber')
    column_searchable_list = ('name','email', 'phonenumber',)
    can_set_page_size = True
    # the number of entries to display in the list view
    page_size = 5
   
class UpdateView(AdminView):
    column_list = ('title', 'date_posted', 'content')
    column_searchable_list = ('title',)
    can_set_page_size = True
    page_size = 5

class UploadView(AdminView):
    column_list = ('img_name', 'user_id', 'date_upload')
    column_searchable_list = ('img_name',)
    can_set_page_size = True
    page_size = 5

class FeedbackView(AdminView):
    column_list = ('first_name', 'last_name', 'email', 'phonenumber')
    column_searchable_list = ('email','first_name', 'last_name')
    can_set_page_size = True
    page_size = 10




# News and updates database

class Update(db.Model):
    __tablename__ = 'updates'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    def __init__(self, title, content, author):
        self.title=title
        self.content=content
        self.date_posted=datetime.now(timezone.utc)
        self.author=author

    def __repr__(self):
        return f"Update('{self.title}',{self.content}', '{self.date_posted}')"           




#Upload image
class UploadImg(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    img_name=db.Column(db.String(300), nullable=False)
    desc=db.Column(db.Text())
    date_upload=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, img_name,desc, author):
        self.img_name=img_name
        self.desc=desc
        self.author=author
        self.date_upload=datetime.now(timezone.utc)

    def __repr__(self):
        return f"UploadImg('{self.img_name}', {self.desc}' )"      




