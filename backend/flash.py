from flask import Flask, request
from db.py import send_message_DB, get_messages

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    message = request.args.get('message')  # Get 'message' from the query params

    send_message_DB(message)

    # if messages contains @readcap get db
    if message.contains('@readcap'):
        ai_response = read_chat(get_messages(), message)
        return ai_response
    else:
        return "nothing"
