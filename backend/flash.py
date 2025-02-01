from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = request.args.get('message')  # Get 'message' from the query params
    return 'Hello from Flask!'

