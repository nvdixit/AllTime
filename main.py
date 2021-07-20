from datetime import datetime
from flask import Flask, jsonify
app = Flask(__name__)

CONST_EST_GMT_DIFF = 5
HOUR_COUNT_ONE = 24
HOUR_COUNT_TWO = 12
DAYLIGHT_SAVINGS = True

all_times = {
    "MIT": "",
    "HST": "",
    "AST": "",
    "PST": "",
    "MST": "",
    "CST": "",
    "EST": "",
    "PRT": "",
    "CNT": "",
    "AGT": "",
    "GST": "",
    "CAT": "",
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
    "NST": ""
}


@app.route("/")
def base_return():
    return "If you're seeing this message, it means you've got the right URL, but not a valid endpoint. " \
           "Head back to the docs page to find valid endpoints"


@app.route("/twenty_four_times")
def twenty_four_times():
    now = datetime.now()
    current_time_24 = now.strftime("%H:%M:%S")

    gmt_hour = (int(current_time_24.split(":")[0]) + CONST_EST_GMT_DIFF) % HOUR_COUNT_ONE
    minute = str(current_time_24.split(":")[1])
    second = str(current_time_24.split(":")[2])

    count = -12
    for key in all_times:
        final_time = str((gmt_hour + count) % HOUR_COUNT_ONE) + ":" + minute + ":" + second

        if DAYLIGHT_SAVINGS:
            if key.__eq__("PST") | key.__eq__("MST") | key.__eq__("CST") | key.__eq__("EST"):
                final_time = str((gmt_hour + count + 1) % HOUR_COUNT_ONE) + ":" + minute + ":" + second

        all_times[key] = final_time
        count += 1

    return jsonify(all_times)


@app.route("/twelve_times")
def twelve_times():
    now = datetime.now()
    current_time_24 = now.strftime("%H:%M:%S")

    gmt_hour = (int(current_time_24.split(":")[0]) + CONST_EST_GMT_DIFF) % HOUR_COUNT_ONE
    minute = str(current_time_24.split(":")[1])
    second = str(current_time_24.split(":")[2])

    count = -12
    for key in all_times:
        final_time = ""
        hour = gmt_hour + count

        if DAYLIGHT_SAVINGS:
            if key.__eq__("PST") | key.__eq__("MST") | key.__eq__("CST") | key.__eq__("EST"):
                hour += 1

        if hour >= 12:
            final_time = str(hour % 12) + ":" + minute + ":" + second + " PM"
        else:
            if hour == 0:
                final_time = "12" + ":" + minute + ":" + second + " AM"
            else:
                final_time = str(hour) + ":" + minute + ":" + second + " AM"

        all_times[key] = final_time
        count += 1

    return jsonify(all_times)


if __name__ == '__main__':
    app.run()
