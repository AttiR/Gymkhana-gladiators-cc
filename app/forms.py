from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms import ValidationError, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp

class FeedbackForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])                       
    email = StringField('Email',
                        validators=[DataRequired(),Length(1, 64), Email()])
    feedback = TextAreaField("Feedback", validators=[DataRequired()])
    submit = SubmitField('Send')                    