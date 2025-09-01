from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, timedelta


def say():
    print("Ежедневная задача")

scheduler = BackgroundScheduler()
scheduler.add_job(say, 'cron', hour=19, minute=3) # запустится через пять секунд после запуска
scheduler.add_job(
    say,
    'cron', 
    day_of_week="mon,wen",
    months='1,2',
    hour='8-18/2', 
    minute=0) # каждый понедельник и среду с 8 до 18 каждые два часа в январе и феврале
scheduler.start()

while True: # функция бесконечности
    pass

