from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email



# Login form class

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Length(1, 64),  Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=7, max=15)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')     

