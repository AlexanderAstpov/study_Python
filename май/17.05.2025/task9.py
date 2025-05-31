s = input("Ведите название файла:  ")

try:
    fl = open(s ,"r",encoding="utf-8")
    print(fl.read())
    fl.close()
except:
    print("Файл не найден")