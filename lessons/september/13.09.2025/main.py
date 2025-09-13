import requests
from bs4 import BeautifulSoup # библиотека для парсинга beautifulsoup4


url = "https://quotes.toscrape.com/"
response = requests.get(url)
# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml") # "lxml" преобразовывает парсинг в подходящий формат
# print(soup.text) показывает очищенный текст
#print(soup.prettify()) #  приобразовывает страницу в красивый и читаемый вид

# Парсим цитаты
quote = soup.find("div", class_= "quote")
# print(quote.text)
# print(quote.prettify())

quote_text = quote.find("span", class_= "text").get_text(strip=True) # обрезает все лишнее и показывает только нужный текст
#print(quote_text.prettify()) # покажет кусок кода, работает без часть кода .get_text(strip=True)
quote_author = quote.find("small", class_="author").get_text(strip=True)
print(quote_text)
print(quote_author)