import os
import secrets
from  flask import current_app
from PIL import Image
from itsdangerous import URLSafeTimedSerializer

# generate Token for user authentication

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email


# save picture function
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) #f_name=_
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img/profileimg', picture_fn)

    # inorder to recize images we will use package pillow
    #pip install pillow
    picture_size=(200, 200)
    s=Image.open(form_picture)
    s.thumbnail(picture_size)

    #form_picture.save(picture_path) 
    s.save(picture_path)
    


    return picture_fn    