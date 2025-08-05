class Lst:
    def __init__(self):
        self.numbers = []


    def add_number(self):
        num = int(input("Введите число: "))
        if num in self.numbers:
            print("Это число уже есть в списке")
        else:
            self.numbers.append(num)
            print("Число успешно добавлено")
    
    def remove_number(self):
        num = int(input("Введите число для удаления: "))
        self.numbers[:] = [x for x in self.numbers if x != num]
        print("Все вхождения числа удалены")
    
    
    def show_list(self):
        direction = input("Если с начала списка введите - н, если с конна введите - к: ")
        if direction == "н":
            print(self.numbers)
        elif direction == "к":
            print(self.numbers)
    
    
    def check_value(self):
        num = int(input("Введите число для проверки: "))
        if num in self.numbers:
            print("Значение есть в списке")
        else:
            print("Значение отсутствует в списке")
    
    
    def replace_value(self):
        num = int(input("Введите число для замены: "))
        replace_num = int(input("Введите новое число: "))
        replace_all = input("Заменить все совпадения? (да/нет): ")
        if replace_all == "да":
            self.numbers = [replace_num if x == num else x for x in self.numbers]
        else:
            index = self.numbers.index(num)
            self.numbers[index] = replace_num
        print("Значение успешно заменено")
 
def show_menu(): 
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")

l = Lst()
 
while True:
    show_menu()
    choice = input("Выберите пункт меню: ")
 
    if choice == "1":
      
       l.add_number()
    elif choice == "2":
       
        l.remove_number()
    elif choice == "3":
      
        l.show_list()
    elif choice == "4":
     
        l.check_value()
    elif choice == "5":
    
        l.replace_value()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")