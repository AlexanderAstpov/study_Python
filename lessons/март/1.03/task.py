print("Введите номер месяца")
month = int(input())
if month == 1 or month == 2 or month == 12:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print ("Summer")
elif month ==9 or month == 10 or month == 11:
    print("Autumn")

else:
    print ("Ошибка!")