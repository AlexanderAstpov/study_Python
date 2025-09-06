import requests 
import json


url = 'https://jsonplaceholder.typicode.com/users/1'

params = {
    'postId': 1
}

response = requests.get(url, params)

data = response.json()

print(json.dumps(data, indent=4, ensure_ascii=False))

 

