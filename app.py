import json, html
from flask import Flask, jsonify




app = Flask(__name__)

# read file
with open('booking-system\data.json', 'r') as myfile:
    data = json.load(myfile)
#

@app.route("/")
def index():
    return jsonify(data["venue"])


if __name__ == "__main__":
    app.run(debug=True, port=8000)