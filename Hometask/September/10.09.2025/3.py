from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def hello(name):
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Привет, {name}! ")

def schedule_hello(scheduler, name_to_pass):

    scheduler.add_job(hello, 'interval', seconds=7, args=[name_to_pass])

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    schedule_hello(scheduler, 'Аня')

scheduler.start()