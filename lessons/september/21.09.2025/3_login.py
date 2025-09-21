from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


driver = webdriver.Chrome()

driver.get("https://practice.expandtesting.com/login")

input_username = driver.find_element(By.ID, "username")
input_password = driver.find_element(By.ID, "password")

input_username.clear() # очистка поля для ввода
input_password.clear()

input_username.send_keys("practice") # передаем логин
input_password.send_keys("SuperSecretPassword!") # передаем пароль

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']") # <button type="submit" class="btn btn-bg btn-primary d-block w-100">Login</button>
login_button.click()

wait = WebDriverWait(driver, 15)
try:
    wait.until(expected_conditions.url_contains("/secure"))
    print("Успешный логин")
except Exception:
    print("Не удалось зайти на сайт")
finally:
    time.sleep(15)
    driver.close()

