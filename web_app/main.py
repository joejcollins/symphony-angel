''' main application '''

import json
import logging
from flask import Flask, render_template, request
from google.appengine.api import mail

app = Flask(__name__) # pylint: disable=invalid-name

@app.route('/')
def hello():
    ''' Just a test message '''
    return 'Hello World!'

@app.route('/form')
def form():
    ''' Show the message form '''
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    ''' Respond to the message submission '''
    email = request.form['email']
    message = request.form['message']
    send_mail() # Send
    return render_template(
        'submitted_form.html',
        email=email,
        message=message)

def send_mail():
    ''' Send an email message '''
    secrets_file = open('secrets.json', 'r')
    secrets = json.loads(secrets_file.read())
    secrets_file.close()
    message = mail.EmailMessage(
        sender="a@b.com",
        subject="Your account has been approved")
    message.to = secrets['email'],
    message.body = "Dear Albert"
    message.send()

# @app.errorhandler(500)
# def server_error(error):
#     ''' Log any errors and send 500 '''
#     # Log the error and stacktrace.
#     logging.exception('An error occurred during a request. ' + error)
#     return 'An internal error occurred.', 500
