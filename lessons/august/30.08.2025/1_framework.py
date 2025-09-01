import requests # библиотека дла http запросов


url = 'https://www.google.com'

response = requests.get(url)
 

print(f'Код ответа: {response.status_code}')
# print(f'Заголовки: {response.headers}')
# print(f'Заголовки: ')
# for key, value in response.headers.items():
#     print(f'{key}:{value}')
# print(f'Тело страницы: {response.content}') # не преобразованная строка
print(f'Тело страницы: {response.text}') # текст можно копировать


with open("google.html", "w", encoding="utf-8") as fl:
    fl.write(response.text)
