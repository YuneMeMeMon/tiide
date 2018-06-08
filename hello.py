from flask import Flask

app = Flask(__name__)

@app.route("/Yune")
def Yune():
    return "Hello World"
