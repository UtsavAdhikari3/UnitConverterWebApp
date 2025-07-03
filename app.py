from flask import Flask
from flask import render_template, request
from flask import jsonify

app = Flask(__name__)

@app.route("/",methods = ["GET"])
def hello():
    return render_template("hello.html")


@app.route("/read-form",methods = ["POST"])
def read_form():
    data = request.form
    print(data)
    return jsonify(data)

