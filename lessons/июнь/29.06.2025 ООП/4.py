class Auto:
    def __init__(self, form, color, power):
        self.form = form
        self.color = color
        self.power = power
        self.producer = "Germany"

        if power <= 150:
            self.__tax = 5000
        elif power > 150 and power <=200:
            self.__tax = 15000
        else:
            self.__tax = 50000
            # защита от изменений

    def show_tax(seif):
        return seif.__tax
        
    

bmw = Auto("sedan", "white", 200)
print(bmw.color)
print(bmw.show_tax())# вывод налога на консоль через функцию
