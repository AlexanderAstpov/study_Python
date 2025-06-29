class Auto:
    def __init__(self):
        self.form = "sedan"
        self.color = "white"
        self.power = 200
        
    

bmw = Auto()

print(bmw)
print(bmw.form)
print(bmw.color)
print(bmw.power)

bmw.power = 250
print(bmw.power)


audi = Auto()
print(audi.power)
