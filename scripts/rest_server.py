import sys
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

# GET method to retrieve data
@app.route('/arv/get', methods=['GET'])
def arv_get():
    if bool(random.getrandbits(1)):
        return jsonify({"Lucky": "Have a nice day"}), 200
    else:
        return jsonify({"Unlucky": "May the task be with you"}), 400

# POST method to add data
@app.route('/arv/post', methods=['POST'])
def arv_post():
    if bool(random.getrandbits(1)):
        return jsonify({"Lucky": "Have a nice day"}), 200
    else:
        return jsonify({"Unlucky": "May the task be with you"}), 400

# PUT method to update data
@app.route('/arv/put', methods=['PUT'])
def arv_put():
    if bool(random.getrandbits(1)):
        return jsonify({"Lucky": "Have a nice day"}), 200
    else:
        return jsonify({"Unlucky": "May the task be with you"}), 400

if __name__ == '__main__':
    try:
        _port_number = int(sys.argv[1])
    except IndexError:
        _port_number = 2000 
    app.run(debug=True, port=_port_number)
