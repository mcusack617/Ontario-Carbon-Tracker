from flask import Flask

app = Flask(__name__)

app.route("/")
def home():
    pass

app.route("/login")
def login():
    pass
