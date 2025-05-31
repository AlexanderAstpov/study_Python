salary = 200
prize = 200
a = 0.03
b = 0.05
c = 0.08

staff1 = int(input("Введите сумму продаж перввого менеджера - "))
staff2 = int(input("Введите сумму продаж второго менеджера - "))
staff3 = int(input("Введите сумму продаж третьего менеджера - "))

if staff1 >= 1000:
    staff1 = staff1 * c + salary
elif  500 < staff1 < 1000:
    staff1 =staff1 * b + salary
elif staff1 <= 500:
    staff1 =staff1 * a + salary

if staff2 >= 1000:
    staff2 = staff2 * c + salary
elif  500 < staff2 < 1000:
    staff2 = staff2 * b + salary
elif staff2 <= 500:
    staff2 = staff2 * a + salary

if staff3 >= 1000:
    staff3 = staff3 * c + salary
elif  500 < staff3 < 1000:
    staff3 = staff3 * b + salary
elif staff3 <= 500:
    staff3 = staff3 * a + salary

if (staff1 > staff2 and staff1 > staff3):
    staff1 = staff1 + 200
elif staff2 > staff3:
       staff2 = staff2 + 200
else:
        staff3 = staff3 + 200   

print("Зарплата первого менеджера равна ", staff1)
print("Зарплата второго менеджера равна ",staff2)
print("Зарплата третьего менеджера равна ",staff3)
