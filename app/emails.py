from flask import current_app
from . import mail
from flask_mail import Message

def send_email(to, subject, template):
  
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=current_app.config['MAIL_USERNAME']
    )
    mail.send(msg)