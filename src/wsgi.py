from flask import Flask, make_response
import cal
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def my_func():
    print("echo hi")

scheduler.add_job(my_func) # Run once immediately
scheduler.add_job(my_func, "interval", minutes=1)
scheduler.start()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/stadalliansen.ics")
def ics():
    response = make_response(cal.calendar.to_ical().decode("ascii"), 200)
    response.mimetype = "text/calendar"
    return response
