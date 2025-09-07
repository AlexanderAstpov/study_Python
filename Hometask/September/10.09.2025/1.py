from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta

n = datetime.now()

def say():
    print(f"[{n.strftime('%Y-%m-%d %H:%M:%S')}]", "Работа в фоне!")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'date', run_date= datetime.now() + timedelta(seconds=10)) 
scheduler.start()

while True:
    time.sleep(2)
    