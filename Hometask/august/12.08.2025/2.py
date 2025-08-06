import json


item ={
"product": "Laptop",
"price": 1200,
"in_stock": True
}

with open("data.json", "w", encoding="utf-8") as fl:
    json.dump(item, fl)


with open("data.json", "r", encoding="utf-8") as fl:
    it = json.load(fl)
    for key, value in item.items():
        print(f"{key.capitalize()}: {value}")
       
        