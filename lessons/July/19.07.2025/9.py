# атребуты класса

class Car:
    count = 0
    def __init__(self, name, power):
        Car.count += 1
        self.name = name
        self.power = power
        self.serial_num = Car.count

    def __str__(self):
        return f"Имя - {self.name}\nМощность -{self.power}\nКол-во созданный машин - {self.count}\nСерийный номер - {self.serial_num}"
    

car1 = Car("Tesla", 500)
car2 = Car("Mersedes", 350)
print(car1)
print(car2)

