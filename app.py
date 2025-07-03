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

    elif form_id == "temperature":
        result = convert_temperature(data)
    reply = {
        "formId": form_id,
        "input":  data,
        "result":result
    }
    return jsonify(reply), 200


def convert_length(data):
    from_unit = data["fromLength"]
    to_unit = data["to"]
    value = float(data["lengthValue"])

    if from_unit == "m" and to_unit == "km":
        result = value / 1000
    elif from_unit == "m" and to_unit == "mi":
        result = value / 1609.344
    elif from_unit == "km" and to_unit == "m":
        result = value * 1000
    elif from_unit == "km" and to_unit == "mi":
        result = value * 0.621371
    elif from_unit == "mi" and to_unit == "m":
        result = value * 1609.344
    elif from_unit == "mi" and to_unit == "km":
        result = value / 0.621371
    elif from_unit == to_unit:
        result = value
    else:
        return {"error": "Unsupported length conversion"}

    return {
        "final_result": "{:.2f}".format(result)
    }


def convert_weight(data):
    from_unit = data["fromWeight"]
    to_unit = data["to"]
    value = float(data["weightValue"])

    if from_unit == "kg" and to_unit == "g":
        result = value * 1000
    elif from_unit == "kg" and to_unit == "lb":
        result = value * 2.20462
    elif from_unit == "g" and to_unit == "kg":
        result = value / 1000
    elif from_unit == "g" and to_unit == "lb":
        result = value * 0.00220462
    elif from_unit == "lb" and to_unit == "kg":
        result = value / 2.20462
    elif from_unit == "lb" and to_unit == "g":
        result = value / 0.00220462
    elif from_unit == to_unit:
        result = value
    else:
        return {"error": "Unsupported weight conversion"}

    return {
        "final_result": "{:.2f}".format(result)
    }


def convert_temperature(data):
    from_unit = data["fromTemp"]
    to_unit = data["to"]
    value = float(data["tempValue"])

    if from_unit == "c" and to_unit == "f":
        result = (value * 9/5) + 32
    elif from_unit == "c" and to_unit == "k":
        result = value + 273.15
    elif from_unit == "f" and to_unit == "c":
        result = (value - 32) * 5/9
    elif from_unit == "f" and to_unit == "k":
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == "k" and to_unit == "c":
        result = value - 273.15
    elif from_unit == "k" and to_unit == "f":
        result = (value - 273.15) * 9/5 + 32
    elif from_unit == to_unit:
        result = value
    else:
        return {"error": "Unsupported temperature conversion"}

    return {
        "final_result": "{:.2f}".format(result)
    }
