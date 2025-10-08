from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com")

data = []

for quote in driver.find_elements(By.CLASS_NAME, "product_pod"):
    text = quote.find_element(By.CSS_SELECTOR, "h3 a").text
    price = quote.find_element(By.CLASS_NAME, "price_color").text

    d ={"title": text, "price": price}
    data.append((d))
    

time.sleep(5)
driver.quit()
print(data)


 