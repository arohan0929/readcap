from flask import Flask, request
from db.py import send_message_DB, get_messages

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    message = request.args.get('message')  # Get 'message' from the query params

    send_message_DB(message)

    # if messages contains @readcap get db

    old_messages = get_messages()

    # new message
    # send back as a response to the api 

    return 'Hello from Flask!'

