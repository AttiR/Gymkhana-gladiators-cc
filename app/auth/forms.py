from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User
from flask_login import current_user

    

# Registration class
class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20),Regexp('^[A-Za-z][A-Za-z0-9_. ]*$', 0,
               'The name contains only letters, spaces, numbers, periods, or underscores')])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    email = StringField('Email',
                        validators=[DataRequired(),Length(10, 64), Email(message="This is not a valid email")])
    phonenumber = StringField('Phonenumber', validators=[DataRequired(),Length(5, 15),
        Regexp('^[0-9]*$', 0, 'for phonenumber only numbers')])                    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15),EqualTo('re_password', message='Passwords must match.')])
    re_password = PasswordField('Type Password again', validators=[DataRequired(), Length(min=7, max=15)])
    submit = SubmitField('Sign Up')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
           raise ValidationError('Username already in use.')

    def validate_username(self, field):
        if User.query.filter_by(phonenumber=field.data).first():
            raise ValidationError('phonenumber already in use.')        

# Login form class

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Length(1, 64),  Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')     


# Password Reset Form
class PasswordresetForm(FlaskForm): 
    
    new_password = PasswordField('New Password', validators=[DataRequired(),Length(min=7, max=15)])
    re_password = PasswordField('Type Password again', validators=[DataRequired(), Length(min=7, max=15)])
    submit = SubmitField('Reset Password') 



# Account Update
class UpdateAccountForm(FlaskForm):
    
    email = StringField('Email',
                        validators=[DataRequired(),Length(10, 64), Email(message="This is not a valid email")])
    phonenumber = StringField('Phonenumber', validators=[DataRequired(),Length(5, 15),
        Regexp('^[0-9]*$', 0, 'for phonenumber only numbers')])                    
   
    submit = SubmitField('Update Profile')


   

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')  

    def validate_phonenumber(self, phonenumber):
        if phonenumber.data != current_user.phonenumber:
            user = User.query.filter_by(phonenumber=phonenumber.data).first()
            if user:
                raise ValidationError('That phone already exists Please enter a different one.')              


