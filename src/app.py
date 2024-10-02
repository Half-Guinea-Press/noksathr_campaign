from flask import Flask

app = Flask(__name__)
server = app.server

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
