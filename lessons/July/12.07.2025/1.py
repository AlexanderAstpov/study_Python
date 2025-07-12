class Auto:
    def __init__(self, mark):
        self.mark = mark


    def __str__(self):
        return f"автомобиль марки - '{self.mark}'"
        

car = Auto("BMW")
print(car.mark)
print(car)