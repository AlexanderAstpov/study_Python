dct = {
    "a": 1,
    "b": 2,
    "c": 3,
    
}

dct["d"] = 4


print("список ключей:", *list(dct.keys()))
print("список значений:", *list(dct.values()))

new_dct = {value:key for key, value in dct.items()}
print(f"перевернутый список {new_dct}")