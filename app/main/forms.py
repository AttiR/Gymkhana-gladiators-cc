from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,  TextAreaField
from wtforms.validators import DataRequired, Length, Email


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


