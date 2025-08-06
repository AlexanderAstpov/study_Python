import json

people =[
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"}
]


new_people = {}
new_people["username"] = input("Введите логин: ")
new_people["email"] = input("Введите email: ") 
people.append(new_people)

with open("users.json", "w", encoding="utf-8") as fl:
    json.dump(people, fl)

with open("users.json", "r", encoding="utf-8") as fl:
    it = json.load(fl)
    



print(it)