from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms import ValidationError, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp

#Feedback class
class FeedbackForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])                       
    email = StringField('Email',
                        validators=[DataRequired(),Length(1, 64), Email()])
    feedback = TextAreaField("Feedback", validators=[DataRequired()])
    submit = SubmitField('Send')     

# Registration class
class RegistrationForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Length(10, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15)])
    re_password = PasswordField('Type Password again', validators=[DataRequired(), Length(min=7, max=15)])
   
    submit = SubmitField('Sign Up')

# Login form class

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Length(1, 64),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')                   