import json

person = {
"name": "Alice",
"age": 25,
"city": "New York"
}

with open("person.json", "w", encoding="utf-8") as fl:
    json.dump(person, fl)
