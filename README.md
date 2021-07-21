# AllTime Documentation

Welcome to AllTime! A RESTful service that returns the current time in every (or one) time zone on Earth. 
To get started, here is the base URL of the API: https://alltime-us.com/

After the base URL, add on one of the following extensions:
  1. twenty_four_times
  2. twelve_times
  3. request_time_24/TIMEZONE
  4. request_time_12/TIMEZONE
  
1:
https://alltime-us.com/twenty_four_times - Returns a JSON of current time in every time zone on Earth in 24-hour time, like so:
 {
    "MIT": "00:00:00",
    "HST": "01:00:00",
    "AST": "02:00:00",
    "PST": "03:00:00",
    "MST": "04:00:00",
    "CST": "05:00:00",
    "EST": "06:00:00",
    "PRT": "07:00:00",
    "CNT": "08:00:00",
    "AGT": "09:00:00",
    "GST": "10:00:00",
    "CAT": "11:00:00",
    "GMT": "12:00:00",
    "ECT": "13:00:00",
    "EET": "14:00:00",
    "EAT": "15:00:00",
    "NET": "16:00:00",
    "PLT": "17:00:00",
    "BST": "18:00:00",
    "VST": "19:00:00",
    "CTT": "20:00:00",
    "JST": "21:00:00",
    "AET": "22:00:00",
    "SST": "23:00:00",
    "NST": "00:00:00",
}

2:
https://alltime-us.com/twelve_times - Returns a JSON of current time in every time zone on Earth in 12-hour time, like so:
{
    "MIT": "00:00:00 AM",
    "HST": "01:00:00 AM",
    "AST": "02:00:00 AM",
    "PST": "03:00:00 AM",
    "MST": "04:00:00 AM",
    "CST": "05:00:00 AM",
    "EST": "06:00:00 AM",
    "PRT": "07:00:00 AM",
    "CNT": "08:00:00 AM",
    "AGT": "09:00:00 AM",
    "GST": "10:00:00 AM",
    "CAT": "11:00:00 AM",
    "GMT": "12:00:00 PM",
    "ECT": "01:00:00 PM",
    "EET": "02:00:00 PM",
    "EAT": "03:00:00 PM",
    "NET": "04:00:00 PM",
    "PLT": "05:00:00 PM",
    "BST": "06:00:00 PM",
    "VST": "07:00:00 PM",
    "CTT": "08:00:00 PM",
    "JST": "09:00:00 PM",
    "AET": "10:00:00 PM",
    "SST": "11:00:00 PM",
    "NST": "00:00:00 AM",
}

3:
https://alltime-us.com/request_time_24/TIMEZONE - Returns the current 24-hour time in the requested TIMEZONE
For example: 
https://alltime-us.com/request_time_24/MIT would return {"MIT": "00:00:00"}
https://alltime-us.com/request_time_24/HST would return {"HST": "01:00:00"}

4:
https://alltime-us.com/request_time_12/TIMEZONE - Returns the current 12-hour time in the requested TIMEZONE
For example: 
https://alltime-us.com/request_time_12/PST would return {"PST": "00:00:00 AM"}
https://alltime-us.com/request_time_12/EAT would return {"EAT": "01:00:00 AM"}

List of time zones adapted from https://publib.boulder.ibm.com/tividd/td/TWS/SC32-1274-02/en_US/HTML/SRF_mst273.htm
