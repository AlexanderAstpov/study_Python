class WaterHeater:
    def __init__(self):
        self.__temperatura = 20
               
           
    @property
    def temperatura(self):
        return self.__temperatura 
    
    @temperatura.setter
    def temperatura(self, new_temperatura):
        if  0 < new_temperatura < 100:
            self.__temperatura = new_temperatura
        else:
            print("Недопустимая темпиратура")

        
    
    def heat_up(self, delta): 
        if self.__temperatura + delta > 100:
            self.__temperatura = 100
        else:
            self.__temperatura += delta
        
    
        


    
heater = WaterHeater()
print(heater.temperatura)
heater.heat_up(10)
print(heater.temperatura)

heater.temperatura = 150




