from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def helloworld():
    message = "my name is deborah"
    addition = "i am pleased to meet you"
    statement = f"Hello world {message} {addition}"
    name = "Deborah"
    age = 5
    location = "Ibadan"
    return jsonify({
        "Name ":name,
        "Age ":age,
        "Location ":location
    })

@app.route("/state")
def current_state():
    state = "Oyo"
    capital = "Ibadan"
    country = "Nigeria"
    return jsonify({
    "State": state,
    "Capital":capital,
    "Country":country

    })