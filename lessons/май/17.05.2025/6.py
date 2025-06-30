def check_age(age):
    if age < 18:
        raise ValueError("Вазраст должен быть > 18 лет")
    elif age > 100:
        raise ValueError("Уже поздно!")
    
age = int(input("введите свой возраст:  "))
try:
    check_age(age)
except Exception as e:
    print(e)