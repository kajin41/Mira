import boto3
from config import AWS_DBADMIN_ACCESS_KEY, AWS_DBADMIN_SECRET_KEY
from datetime import datetime

client = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_DBADMIN_ACCESS_KEY,
    aws_secret_access_key=AWS_DBADMIN_SECRET_KEY,
    region_name='us-east-1'
)


def create_signup_entry(name, email, type):
    table = client.Table('signups')
    table.put_item(
        Item={
            'email': email,
            'name': name,
            'timestamp': str(datetime.now()),
            'type': type
        }
    )


def create_contact_entry(name, email, subject, message):
    table = client.Table('contact')
    table.put_item(
        Item={
            'email': email,
            'name': name,
            'subject': subject,
            'message': message,
            'timestamp': str(datetime.now()),
        }
    )
