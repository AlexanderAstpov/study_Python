class Auto:
    def __init__(self, name, year,power, color, price):
        self.name = name
        self.year = year
        self.producer = "Germany"
        self.power = power
        self.color = color
        self.price = price
 

bmw = Auto("s8","2025" "sedan", 200, "white", 65000)
print(f"BMW - Цвет-{bmw.color}, Мощность-{bmw.power}, Модель-{bmw.name}")

