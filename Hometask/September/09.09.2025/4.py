import requests 
import json


url = 'https://jsonplaceholder.typicode.com/posts'

payload = {
        'title': 'Мой заголовок',
        'body': 'Текст',
        'userId': 5
    }
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

posts = response.json()
print(f"Created post ID:- {posts['id']}")
print("Запрос успешно выполнен: ", response.text)



 

