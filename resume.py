from flask import Flask, render_template, request, redirect
from mail import signup_thank_you, contact_email
from database import create_signup_entry, create_contact_entry
import requests
import config
import json

app = Flask(__name__)


nav_items = ['app', 'join', 'about', 'partners', 'contact']


@app.route('/')
def index():
    return render_template("home3.html", title="MiraSaves", nav_items=nav_items)


@app.route('/signup', methods=["POST"])
def patient_signup():
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      data={'secret': config.captcha_secret_key,
                            'response': request.form['g_recaptcha_response'],
                            'remoteip': request.headers['X-Forwarded-For']})

    google_response = json.loads(r.text)
    print('JSON: ', google_response)

    if google_response['success']:
        print('captcha SUCCESS')
        name = request.form['name']
        email = request.form['email']
        signup_type = request.form['type']
        create_signup_entry(name, email, signup_type)
        signup_thank_you(name, email, signup_type)
        return "Thanks For Signing up, You Will Receive an e-Mail Shortly"
    else:
        return "oops something went wrong."


@app.route('/contact', methods=["POST"])
def contact():
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      data={'secret': config.captcha_secret_key,
                            'response': request.form['g-recaptcha-response'],
                            'remoteip': request.headers['X-Forwarded-For']})

    google_response = json.loads(r.text)
    print('JSON: ', google_response)

    if google_response['success']:
        print('captcha SUCCESS')
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        create_contact_entry(name, email, subject, message)
        contact_email(name, email, subject, message)
        return "Thanks For Contacting Us, You Will Receive an e-Mail Shortly"
    else:
        return "oops something went wrong."
#logic



if __name__ == '__main__':
    app.run()
