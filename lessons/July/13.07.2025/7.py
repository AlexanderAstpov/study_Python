class Car:
    def __init__(self, mark, color, year):
        self.mark = mark
        self.color = color
        self.year = year

    def drive(self):
        print("Машина поехала") # метод экземпляра класса

    @classmethod
    def description(cls):
        print("Это класс для создания автомобиля")
        print(cls)

    @classmethod
    def audi(cls, color, year):
        return cls("audi", color, year)

    @staticmethod
    def st():
        print("Привет это статический метод")

    def __str__(self):
        return f'Марка - {self.mark}\nЦвет - {self.color}\nГод выпуска - {self.year}'
    

car1 = Car("BMW", "black", 1981)

print(car1)
car1.drive() # метод экземпляра класса

Car.description()
print()
car2 = Car.audi("White", 1950)
print(car2)

Car.st()
car1.st()