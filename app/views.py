from app import app

from flask import render_template

@app.route("/")
def home():
    print(app.config['ENV'])
    return render_template("public/home.html")

@app.route("/about")
def about():
    return render_template("public/about.html")  

@app.route("/contact")
def contact():
    return render_template("public/contact.html")    

@app.route("/signup")
def signup():
    return render_template("public/signup.html")  

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