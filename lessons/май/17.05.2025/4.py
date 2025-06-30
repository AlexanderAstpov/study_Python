print("Введите любое число:  ")
try:
    number = int(input())
    print(2 * number)
    print(2 / number)
    print(2 + number)
    print(2 - number)
    dct = {
    [1,2,2]: "start",
    }
except ValueError:
    print("Введены не корректные данные")
except ZeroDivisionError:
    print("Ошибка деления на ноль")
except:
    print("Какая то ошибка")
# print(number)