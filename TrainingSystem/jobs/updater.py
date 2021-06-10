from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import remind_participants, test

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(remind_participants, 'interval', hours=24)
	scheduler.start()