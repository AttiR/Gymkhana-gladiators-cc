
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

#Make Post Update
class UpdateForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    submit=SubmitField('Post Update')


# Image Upload

class ImageUpload(FlaskForm):
    description= StringField('Description', validators=[DataRequired()])
    picture = FileField('Choose Picture', validators=[FileAllowed(['jpg', 'png'])])                    
    submit = SubmitField('Upload')

class VideoUpload(FlaskForm):
    description= StringField('Description', validators=[DataRequired()])
    video = FileField('Choose Video Mp4', validators=[FileAllowed(['mp4'])])                    
    submit = SubmitField('Upload')    