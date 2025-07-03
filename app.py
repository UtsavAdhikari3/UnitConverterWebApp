from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template("hello.html")      

@app.route("/read-form", methods=["POST"])
def read_form():
    if request.is_json:
        data = request.get_json(force=True)
    else:
        data = request.form.to_dict()

    form_id = data.get("formId", "length")  

    if form_id == "length":
        result = convert_length(data)
    
    elif form_id == "weight":
        result = convert_weight(data)
    reply = {
        "formId": form_id,
        "input":  data,
        "result":result
    }
    return jsonify(reply), 200


def convert_length(data):
    if data['fromLength'] == "m" and data["to"] == "km":
        value = float(data["lengthValue"])/1000

    elif data['fromLength'] == "m" and data["to"] == "mi":
        value = float(data["lengthValue"])/1609.344

    elif data['fromLength'] == "km" and data["to"] == "m":
        value = float(data["lengthValue"])*1000

    elif data['fromLength'] == "km" and data["to"] == "mi":
        value = float(data["lengthValue"])*0.621371

    elif data['fromLength'] == "mi" and data["to"] == "m":
        value = float(data["lengthValue"])*1609.344

    elif data['fromLength'] == "mi" and data["to"] == "km":
        value = float(data["lengthValue"])/0.621371
    
    else:
        return "Value out of bounds"
    
    converted_length = {
        "final_result" : "{:.2f}".format(value),
    }
    return converted_length        


def convert_weight(data):
    pass