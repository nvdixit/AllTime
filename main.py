from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)

all_times = {
    "GMT": "",
    "ECT": "",
    "EET": "",
    "EAT": "",
    "NET": "",
    "PLT": "",
    "BST": "",
    "VST": "",
    "CTT": "",
    "JST": "",
    "AET": "",
    "SST": "",
    "NST": "",
    "MIT": "",
    "HST": "",
    "AST": "",
    "PST": "",
    "PNT": "",
    "CST": "",
    "EST": "",
    "PRT": "",
    "CNT": "",
    "AGT": "",
    "GST": "",
    "CAT": ""
}


@app.route("/twenty_four_times")
def twenty_four_times():
    now = datetime.now()
    current_time_24 = now.strftime("%H:%M:%S")
    all_times["EST"] = current_time_24

    return jsonify(all_times)


@app.route("/twelve_times")
def twelve_times():
    now = datetime.now()
    current_time_12 = now.strftime("%I:%M:%S %p")
    all_times["EST"] = current_time_12

    return jsonify(all_times)


if __name__ == '__main__':
    app.run()
