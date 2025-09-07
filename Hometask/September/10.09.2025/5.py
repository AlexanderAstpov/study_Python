from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime

def job_1_function():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Задача 1 выполняется.")

def job_2_function():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Задача 2 выполняется.")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()

    # Добавление задач
    scheduler.add_job(job_1_function, 'interval', seconds=5, id='job_1')
    scheduler.add_job(job_2_function, 'interval', seconds=8, id='job_2')

    scheduler.start()
  

    # Пауза для job_1 через 15 секунд
    time.sleep(15)
    scheduler.pause_job('job_1')
    print("задача 1 на паузе.")

    # Удаление обеих задач через 30 секунд
    time.sleep(15)  # Дополнительные 15 секунд после паузы, итого 30
    scheduler.remove_job('job_1')
    scheduler.remove_job('job_2')
    print("Обе задачи удалены.")

    scheduler.shutdown()
    