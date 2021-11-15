from . import main
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, abort
from .forms import FeedbackForm
from ..models import Feedback
from .. import db
#from app import mail
#from flask_mail import Message
from ..emails import send_email

@main.route("/")
def home():
   
   
    return render_template("public/main/home.html")

@main.route("/about")
def about():
    return render_template("public/about.html")  

# Updates routes
@main.route("/update")
def update():
    return render_template("public/updates.html") 
    

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

        # send email for feedback
        # lest set a test varibale
        email_sent = False
        html = render_template('mails/feedback.html', first_name=first_name, last_name=last_name,
        email=email, feedback=feedback)
        subject = "Feedback send/Contact Request"
        send_email('attirehman388@gmail.com', subject, html) #send_emai() from emails.py
        email_sent = True
        if(email_sent):
            #Flash messages
            flash(f'Feedback has been sent, Thank you {first_name}!', 'success') # flash is an easy mthode to send one time alert
            return redirect( url_for('main.contact') )
        else:
           return "email not sent"
     
    return render_template("public/contact.html", form=form)    


@main.route("/gallary")
def gallary():
    return render_template("public/gallary.html")  

@main.route("/club-members")
def members():
    return render_template("public/members.html")     

@main.route("/acheivements")
def acheievments():
    return render_template("public/acheivements.html") 
@main.route("/policy")
def policy():
    return render_template("public/policy.html")   