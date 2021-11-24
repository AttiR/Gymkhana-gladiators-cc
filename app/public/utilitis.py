import os
import secrets
from  flask import current_app
from PIL import Image


# Upload image function picture function
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #f_name=_
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img/upload', picture_fn)

    # inorder to recize images we will use package pillow
    #pip install pillow
    picture_size=(612, 407)
    s=Image.open(form_picture)
    s.thumbnail(picture_size)

    #form_picture.save(picture_path) 
    s.save(picture_path)
    


    return picture_fn   