from flask import Flask

app = Flask(__name__)

app.route("/")
def index():
    return "SAMPLE WEB APP"

app.route("/hello")
def hello():
    return "HELLO MS-RANGERS"
