from flask import Flask, make_response
from . import cal
from apscheduler.schedulers.background import BackgroundScheduler
import tomllib
from . import scraper
import logging
import sys
logger = logging.getLogger(__name__)

def create_app(config_path):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    app = Flask(__name__)
    scheduler = BackgroundScheduler()
    logger.info("Create app")
    logger.info(f"Creating app: config_path={config_path}")
    if app.config.from_file(config_path, load=tomllib.load, text=False):
        logger.info("successfully loaded config")

    def renew_calendar():
        logger.info("renew calendar")
        serviceInfos = []
        try:
            serviceInfos = scraper.get_events_from_source(app.config["USERNAME"], app.config["PASSWORD"])
        except Exception:
            logger.exception("get events from source failed")
        if serviceInfos:
            calendar = cal.from_service_info(serviceInfos)
        else:
            calendar = cal.broken()

        app.config["calendar"] = calendar
        logger.info("renew calendar done")
    renew_calendar()

    @app.route("/")
    def hello_world():
        logger.info("Request hello world")
        return "<p>hello world</p>"

    @app.route("/stadalliansen.ics")
    def ics():
        logger.info("Request ics")
        response = make_response(app.config["calendar"].to_ical().decode("utf-8"), 200)
        response.mimetype = "text/calendar"
        return response

    scheduler.add_job(renew_calendar, "interval", minutes=60)
    scheduler.start()
    return app
