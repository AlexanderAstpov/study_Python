
class Stack:
    def __init__(self):
        self.stack = []
       

    def push(self, string):
        self.stack.append(string)
        print(f"В стек добавленно следующее значение: - {string}")
       

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Стек пуст")

    def count(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        print(f"У нас стек с нефиксированными размерами\nВ стейке - {len(self.stack)} значений")
    
    def _clear(self):
        self.stack = []

    def push_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Стек пустой")
            


def show_meny():
    print("1. Поместить строку в стек")
    print("2. Вытащить строку из стека")
    print("3. Количество строк в стеке")
    print("4. Проверить, пустой ли стек")
    print("5. Проверить, полный ли стек")
    print("6. Очистить стек")
    print("7. Получить значение верхней строки стека без выталкивания")
    print("0. Выход")
        

stack = Stack()



while True:
    show_meny()
    choice = input("Выберите операцию: ")

    if choice == "1":
        string = input("Введите строку: ")
        stack.push(string)
    elif choice == "2":
        popped_string = stack.pop()

        if popped_string:

            print("Извлеченная строка:", popped_string)

    elif choice == "3":

        print("Количество строк в стеке:", stack.count())

    elif choice == "4":

        print("Стек пустой:", stack.is_empty())

    elif choice == "5":

         stack.is_full()

    elif choice == "6":

        stack._clear()

        print("Стек очищен")

    elif choice == "7":
        
        print("Значение верхней строки стека:", stack.push_top())           

    elif choice == "0":

        break

    else:

        print("Некорректный выбор операции")


print("Работа с стеком завершена")



