from . import main
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, abort
from .forms import FeedbackForm
from ..models import Feedback,User, Update
from .. import db
import os
#from app import mail
#from flask_mail import Message
from ..emails import send_email
from flask_login import current_user
from flask import current_app


@main.route("/")
def home():
    print(os.environ.get('SECRET_KEY'))
    updates=Update.query.order_by(Update.date_posted.desc()).limit(3).all() # fetch only first 3
    
    
    return render_template("public/main/home.html", updates=updates)

@main.route("/about")
def about():
    return render_template("public/about.html")  


    

# Contact/Feedback form route
@main.route("/contact", methods=['POST', 'GET'])
def contact():
    # create object from class
    form = FeedbackForm()
    if request.method == 'POST':
        req= request.form
        first_name= req['first_name']
        last_name= req['last_name']
        email=req['email']
        feedback=req['feedback']

        # databse entry
        data = Feedback(first_name, last_name, email, feedback)
        db.session.add(data)
        db.session.commit()
        flash(f'Feedback has been sent, Thank you {first_name}!', 'success')
        return redirect( url_for('main.contact') )

        # send email for feedback
        # lest set a test varibale
        #email_sent = False
        #html = render_template('mails/feedback.html', first_name=first_name, last_name=last_name,
        #email=email, feedback=feedback)
        #subject = "Feedback send/Contact Request"
        #send_email('attirehman388@gmail.com', subject, html) #send_emai() from emails.py
        #email_sent = True
        #if(email_sent):
            #Flash messages
            #flash(f'Feedback has been sent, Thank you {first_name}!', 'success') # flash is an easy mthode to send one time alert
            #return redirect( url_for('main.contact') )
        #else:
           #return "email not sent"
     
    return render_template("public/contact.html", form=form)    

# Glaaalry section
@main.route("/gallary")
def gallary():
    return render_template("public/gallary.html")  

# Club members sections    

@main.route("/club-members", methods=['POST', 'GET'])
def members():
    user = User.query.order_by(User.confirmed_on).all() # how to abstract data from User model
    
    
    return render_template("public/members.html", user=user)     

@main.route("/acheivements")
def acheievments():
    return render_template("public/acheivements.html") 
@main.route("/policy")
def policy():
    return render_template("public/policy.html")   