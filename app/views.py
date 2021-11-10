from app import app

from flask import render_template, request, redirect, url_for, flash
from app.forms import FeedbackForm, RegistrationForm, LoginForm
from app.models import Feedback
from app import db
from app import mail
from flask_mail import Message



@app.route("/")
def home():
    print(app.config['SQLALCHEMY_DATABASE_URI'])
   
    return render_template("public/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")  

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

          # how to sent an email
        msg = Message('Feedback notification', sender = 'attirehman388@gmail.com', recipients = [email])
        msg.body = feedback
        mail.send(msg)
        email_sent = True
        if(email_sent):
            #Flash messages
            flash(f'Feedback has been sent, Thank you {first_name}!', 'success') # flash is an easy mthode to send one time alert
            return redirect( url_for('contact') )
        else:
            return "email not sent"
     

    return render_template("public/contact.html", form=form)    

# Registration route
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form=RegistrationForm()
    if request.method=='POST':
        req=request.form
        name=req['name']
        print(req)
        if form.validate_on_submit():
            flash(f'Account Created for {name}!', 'success') # flash is an easy mthode to send one time alert
        # set the base layout for flash messages at base.html
        return redirect( url_for('signup') )
    return render_template("public/signup.html", form=form)  

@app.route("/login")
def login():
    return render_template("public/login.html")             

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