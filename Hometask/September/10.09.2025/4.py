
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time


def job():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Напоминание! ")
    

sched = BackgroundScheduler()
sched.add_job(job, 'cron', minute=1) 
sched.add_job(
    job,
    'cron',  
    minute='*/1')

sched.start()
time.sleep(180)

