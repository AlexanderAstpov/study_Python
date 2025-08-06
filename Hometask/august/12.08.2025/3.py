import json

people =[
{"name": "Alice", "age": 25},
{"name": "Bob", "age": 30},
{"name": "Charlie", "age": 22}
]

with open("people.json", "w", encoding="utf-8") as fl:
    json.dump(people, fl)

with open("people.json", "r", encoding="utf-8") as fl:
    it = json.load(fl)
    max_age = max(it, key=lambda it: it["age"])
    print(f"Имя старшего из группы - {max_age['name']}, возраст -  {max_age['age']}") 
       
