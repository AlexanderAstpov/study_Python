from dotenv import load_dotenv
import os

load_dotenv()# загрузка переменного окружения из файла .env

api_key = os.getenv("API_KEY")
login = os.getenv("LOGIN", "username_not_exist")
password = os.getenv("PASSWORD", "password_not_exist") # первое слово - это ссылка на переменную и второе это слово каторое подставится если переменная не найдена.

print(api_key)
print(login)
print(password)