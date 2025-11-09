from flask import Flask, make_response
import cal

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/stadalliansen.ics")
def ics():
    response = make_response(cal.calendar.to_ical().decode("ascii"), 200)
    response.mimetype = "text/calendar"
    return response
