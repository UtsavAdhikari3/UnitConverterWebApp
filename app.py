from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def hello():
    return render_template("hello.html")


@app.route("/read-form",methods = ["POST"])
def read_form():
    data = request.form
    print(data)
    return data

