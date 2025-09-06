import datetime
import time

work_duration = 20

interval = 5


start_time = time.time()
while time.time() - start_time < work_duration:
    current_time = datetime.datetime.now()
    print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}]  Сейчас время: {current_time.strftime('%H:%M:%S')}")
    time.sleep(interval)

