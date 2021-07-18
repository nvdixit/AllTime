from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)

# Gets the current time
now = datetime.now()

current_time_24 = now.strftime("%H:%M:%S")
current_time_12 = now.strftime("%I:%M:%S %p")


@app.route("/")
def dummy_return():
    return jsonify(anything="Hello World")


if __name__ == '__main__':
    app.run()
