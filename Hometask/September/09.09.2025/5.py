import requests 
import json


url = 'https://jsonplaceholder.typicode.com/posts/1'

payload = { 
    'title': 'foo',
    }
headers = {'Content-Type': 'application/json; charset=UTF-8' }

response = requests.patch(url, data=json.dumps(payload), headers=headers)
print('Updated title: foo')
print(response.text)


 

