from app import app
from app import mail
from flask_mail import Message

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='attirehman@388@gmail.com'
    )
    mail.send(msg)