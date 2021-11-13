from datetime import datetime
from werkzeug.security import generate_password_hash
from app import app

from flask import render_template, request, redirect, url_for, flash, abort
from app.forms import FeedbackForm,LoginForm, PasswordresetForm
from app.models import Feedback
from app import db
#from app import mail
#from flask_mail import Message
from app.emails import send_email





@app.route("/")
def home():
   
    print(app.config['SECURITY_PASSWORD_SALT'])
    return render_template("public/main/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")  

# Updates routes
@app.route("/update")
def update():
    return render_template("public/updates.html") 
    

# Contact/Feedback form route
@app.route("/contact", methods=['POST', 'GET'])
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
            return redirect( url_for('contact') )
        else:
           return "email not sent"
     
    return render_template("public/contact.html", form=form)    



#Login Route
@app.route("/login", methods=['PSOT', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template("auth/login.html", form=form)   

# Password Reset Route
@app.route("/passwordreset", methods=['PSOT', 'GET'])
def passwodreset():
    form= PasswordresetForm()
    if form.validate_on_submit():
        pass
    return render_template("auth/password_reset.htm", form=form) 


@app.route("/gallary")
def gallary():
    return render_template("public/gallary.html")  

@app.route("/club-members")
def members():
    return render_template("public/members.html")     

@app.route("/acheivements")
def acheievments():
    return render_template("public/acheivements.html") 
@app.route("/policy")
def policy():
    return render_template("public/policy.html")          