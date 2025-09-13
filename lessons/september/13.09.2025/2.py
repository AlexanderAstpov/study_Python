import requests
from bs4 import BeautifulSoup # библиотека для парсинга beautifulsoup4

data = []


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml") 

quotes = soup.find_all("div", class_= "quote") # find_all - отобразит все дивы 
#print(len(quotes)) # посчитал кол-во тегов

for quote in quotes:
    quote_text = quote.find("span", class_= "text").get_text(strip=True) 
    quote_author = quote.find("small", class_="author").get_text(strip=True)

    #print(quote_author.ljust(20, " "), quote_text) # 20 -кол-во символов в строке, " " остальное заполняется пробелами
    d = {"author": quote_author, "quote": quote_text}
    data.append(d)


for elem in data:
    print(elem)