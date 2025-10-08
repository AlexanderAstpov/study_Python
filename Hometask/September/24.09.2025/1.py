import requests
from bs4 import BeautifulSoup
import time
import xlsxwriter
from xlsxwriter.color import Color

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

        d = {"author": quote_author, "quote": quote_text}
        data.append(d)


    next_btn = soup.find("li", class_="next") # ищем кнопку переключения страницы next и саму страницу
    if next_btn: 
        url = base_url + next_btn.a["href"] # a["href"] - адрес строки с кнопкой next
        url = None # парсит только первую строницу для теста
        print(url)
    else:
        url = None # закрываем цикл если не нашли кнопку next




print("--------------------------------------------")
print(f"парсинг завершен, найдено {len(data)} цитат")

# Скрипт для записи в Exel

workbook = xlsxwriter.Workbook("quotes.xlsx") # пример для записи в Exel
worksheet = workbook.add_worksheet("Quotes") # создание вкладки в Exel

# Вариант номер один для колонок
header_format_1 = workbook.add_format(
    {
        "bold": True,
        "border": 2,
        "align": "center",
        "valign": "vcenter",
        "bg_color": Color("Green")
    }
) # форматирование заголовка

header_format_2 = workbook.add_format(
    {
        "bold": True,
        "border": 2,
        "align": "center",
        "valign": "vcenter",
        "bg_color": Color("Blue")
    }
)

text_format_1 = workbook.add_format({
    "border": 1,
    "align": "left",
    "text_wrap": True, # отвечает за перенос строк
    "bg_color": Color("Orange")
})
     

text_format_2 = workbook.add_format({
    "border": 1,
    "align": "left",
    "text_wrap": True, # отвечает за перенос строк
    "bg_color": Color("Pink")
})


# cell_format_3 = workbook.add_format({"bg_color": Color("Orange")})
# cell_format_4 = workbook.add_format({"bg_color": Color("Pink")})



worksheet.set_column(0,0, 25) # устанавливает ширену колонки в промежетке 0 и 0 ширену 25
worksheet.set_column(1,1, 300) # устанавливает ширену колонки в промежетке 1 и 1 ширену 300
worksheet.set_row(0,30) # устанавливает номер строки (0) и высоту строки (30)

# worksheet.write_string(0, 0, color_format)
# # worksheet.write_blank(2, 1, None, color_format)

worksheet.write(0,0, "Author", header_format_1) # по индексу 0 номер строки 0 номер колонки author верхний левый угол
worksheet.write(0,1, "Quote", header_format_2) # по индексу 0 номер строки 1 номер колонки 


for row, elem in enumerate(data, start=1): # построчная запись в таблицу из БД начиная с второй строки которая обозначается цыфрой 1
    worksheet.write(row, 0, elem["author"], text_format_1)
    worksheet.write(row, 1, elem["quote"], text_format_2)


workbook.close() 

print("Файл Exel успешно создан!")