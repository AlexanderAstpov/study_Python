worker = {
    "name": "Иван",
    "fname": "Иванов",
    "age": 25,
    "profession": "Баскетболист",
    "salary": 500_000
}

worker["start_date"] = "12.12.12" # it's adding a key and values

print(worker)
print(f"{worker['profession']} по имени {worker['name']} получает зарплату в размере {worker['salary']} рублей")