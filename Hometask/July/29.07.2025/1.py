class Device:
    def __init__(self, type_of):
        self.type_of = type_of

    def __str__(self):
        return f"Divice - {self.type_of}, Name - {self.name}, Power - {self.power}"


class CoffeeMachine(Device):
    def __init__(self, type_of, name, power):
        self.name = name
        self.power = power
        super().__init__(type_of)

    def make_coffe(self):
        print("Варит кофе")


class Blander(Device):
    def __init__(self, type_of, name, power):
        self.name = name
        self.power = power
        super().__init__(type_of)

    def make_mix(self):
        print("Смешивает продукты")

 
class MeatGrinder(Device):
    def __init__(self, type_of, name, power):
        self.name = name
        self.power = power
        super().__init__(type_of)

    def grinder(self):
        print("Делает фарш")


  

a = CoffeeMachine("Coffee Machine", "Bosh", 300)
b = Blander("Blander", "Gorenje", 650)
c = MeatGrinder("MeatGrinder", "Moulinex", 900)
print(a)
a.make_coffe()
print(b)
b.make_mix()
print(c)
c.grinder()