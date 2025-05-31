enter = input("Введите строку:   ")
e = enter.replace(" ", "")
a = e[::-1]
if e.lower() == a.lower():
    print( enter, " -  является палиндромом!")
else:
    print( enter,  " -  не является палиндромом!")

