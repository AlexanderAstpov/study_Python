class Auto:
    def __init__(self, name, year, power, color, price):
        self.__name = name
        self.__year = year
        self.producer = "Германия"
        self.__power = power
        self.__color = color
        self.__price = price

    @property
    def name(self):
        return self.__name
    

    @property
    def year(self):
        return self.__year
    
    def producer(self):
        return self.producer
    
    @property
    def power(self):
        return self.__power
    
    @property
    def color(self):
        return self.__color
    
    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @power.setter
    def power(self, new_power):
        self.__power = new_power

    @color.setter
    def color(self, new_color):
        self.__color = new_color


    @price.setter
    def price(self, new_price):
        self.__price = new_price

    
        
 

car1 = Auto("s8","2025", 200, "white", 65000)
print(car1.name)
print()

car1.name = "A5"
car1.year = 2005

car1.color = "black"
car1.power = 250
car1.price = 60000

print(f"Марка авто - {car1.name}\nГот выпуска - {car1.year}\nЦвет - {car1.color}\nМощность - {car1.power} сл.\nЦена - {car1.price}\nСтрана производителя - {car1.producer}")

