import requests 
import json


url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'userId': 1 
}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    print('Post titles by user 1: ')

    for post in posts:
        print(f"- {post['title']}")
        
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)



 

