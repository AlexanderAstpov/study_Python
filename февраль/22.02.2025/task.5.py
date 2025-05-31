weather = "дождь"
umbrella = "мокрый"
print("Смотрим в окно")
if weather == "дождь":
    print("на улице дождь")
    if umbrella == "мокрый":
        print("Берем плащ")
    else:
        print("Берем зонт")
else:
    print("На улице" , weather)
    print("Берем очки", "Берем панаму", "Берем крем", sep="\n")
print("Идем на улицу")