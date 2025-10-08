from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login")
time.sleep(3)
driver.find_element(By.ID, 'username').send_keys('student')
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.ID, 'submit').click()
time.sleep(5)


info = driver.find_element(By.CLASS_NAME, 'has-text-align-center').text

driver.quit()

print(info)