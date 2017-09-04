from flask import Flask, render_template, request, redirect
from mail import signup_thank_you, contact_email
from database import create_signup_entry, create_contact_entry

app = Flask(__name__)


nav_items = ['app', 'join', 'about', 'partners', 'contact']


@app.route('/')
def index():
    return render_template("home3.html", title="Mira Saves", nav_items=nav_items)


@app.route('/signup', methods=["POST"])
def patient_signup():
    name = request.form['name']
    email = request.form['email']
    signup_type = request.form['type']
    create_signup_entry(name, email, signup_type)
    signup_thank_you(name, email, signup_type)
    return "Thanks For Signing up, You Will Receive an e-Mail Shortly"


@app.route('/contact', methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    create_contact_entry(name, email, subject, message)
    contact_email(name, email, subject, message)
    return "Thanks For Contacting Us, You Will Receive an e-Mail Shortly"

if __name__ == '__main__':
    app.run()
