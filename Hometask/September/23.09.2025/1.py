import requests
from bs4 import BeautifulSoup
import time
import json

data = []

base_url = "https://quotes.toscrape.com"
url = base_url

while url:
    time.sleep(2) # задержка парсинга, лучше ставить от 5 секунд
    response = requests.get(url) # url каждый раз будет новая страница

    soup = BeautifulSoup(response.text, "lxml") 
    quotes = soup.find_all("div", class_= "quote")


    for quote in quotes:
        quote_text = quote.find("span", class_= "text").get_text(strip=True) 
        quote_author = quote.find("small", class_="author").get_text(strip=True)
        links_tags = quote.find_all('meta', class_="keywords")
        link_author = quote.find('a', href= True)
        
        extracted_urls = []
        for link_tag in links_tags:
            link = link_tag.get('content')
            if link:
                extracted_urls.append(link)
        for extracted_url in extracted_urls:
            tegs = extracted_url.split(',')
            new_tags = ', '.join(tegs)
            print(new_tags)


        if link_author:
            url_author = link_author['href'] 
            l = base_url + url_author
            print(f"URL: {l}")
        else:
            print("Ссылка не найдена.")    
            


        d = {"author": quote_author, "quote": quote_text, "tags": new_tags, "author_url": l}
        data.append(d)


    next_btn = soup.find("li", class_="next") 
    if next_btn: 
        url = base_url + next_btn.a["href"]
        print(url)
    else:
        url = None 


with open("quotes.json", "w", encoding="utf-8") as fl:
    json.dump(data, fl, indent=4, ensure_ascii=False)
        
    

print("--------------------------------------------")
print(f"парсинг завершен, найдено {len(data)} цитат")