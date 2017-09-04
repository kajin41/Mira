import boto3
import config
from flask import render_template

region = 'us-east-1'
user = config.AWS_DBADMIN_ACCESS_KEY  # insert your access key to use when creating the client
pw = config.AWS_DBADMIN_SECRET_KEY  # insert the secret key to use when creating the client
client = boto3.client(service_name='ses',
                      region_name=region,
                      aws_access_key_id=user,
                      aws_secret_access_key=pw)


def signup_thank_you(name, email, type):
    me = 'info@mirasaves.com'
    you = email
    subject = 'Thank You For Signing Up for Mirasaves'
    destination = {'ToAddresses': [you],
                    'CcAddresses': [],
                    'BccAddresses': []}
    try:
        bodyhtml = render_template("signup_thank_you.html", name=name, type=type)
        message = {'Subject': {'Data': subject},
                   'Body': {'Html': {'Data': bodyhtml}}}
    except Exception as e:
        print(e)
    result = client.send_email(Source=me,
                               Destination=destination,
                               Message=message)
    return result if 'ErrorResponse' in result else ''


def contact_email(name, email, subject, message):
    me = 'info@mirasaves.com'
    you = email
    subject = subject
    destination = {'ToAddresses': [me],
                    'CcAddresses': [],
                    'BccAddresses': []}
    try:
        bodyhtml = you + '<br>' + message
        message = {'Subject': {'Data': subject},
                   'Body': {'Html': {'Data': bodyhtml}}}
    except Exception as e:
        print(e)
    result = client.send_email(Source=name + '<' + me + '>',
                               Destination=destination,
                               Message=message)
    return result if 'ErrorResponse' in result else ''
