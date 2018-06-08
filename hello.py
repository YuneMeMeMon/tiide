from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/Yoon")
def Yoon():
    return "Hello Yoon Me Me Mon"
    
