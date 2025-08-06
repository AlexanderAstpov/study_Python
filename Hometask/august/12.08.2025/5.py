import json

my_dict ={
    "host": "localhost",
    "port": 8080
}

key_to_check = "debug"

with open("config.json", "w", encoding="utf-8") as fl:
    json.dump(my_dict, fl)

with open("config.json", "r", encoding="utf-8") as fl:
    it = json.load(fl)
if key_to_check in my_dict:
    print(f"Ключ '{key_to_check}' найден в словаре")
else:
    my_dict[key_to_check] = False
    with open("config.json", "w", encoding="utf-8") as fl:
        json.dump(my_dict, fl)
    print(my_dict)

 

