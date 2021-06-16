from flask import Flask, request, jsonify

app = Flask(__name__)

values = {

}


@app.route('/set_val', methods=['POST'])
def set_route():

    prop = request.headers["prop"]
    val = request.headers["val"]

    values[prop] = val

    return ""


@app.route('/get')
def get_route():
    return jsonify(values)
