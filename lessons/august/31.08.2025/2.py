from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime



def say_hello():
    print("hello from code, time:", datetime.now().time())

def inform():
    print('---ENFORMATION---')

scheduler = BlockingScheduler()

scheduler.add_job(say_hello, 'interval', seconds=5)
scheduler.add_job(inform, 'interval', seconds=2)
scheduler.start() #запуск программы
# BlockingScheduler блкирующий планировщик, дальше программу дописать и запустить нельзя. 