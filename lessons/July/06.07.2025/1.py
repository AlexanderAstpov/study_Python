from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = radius * 2
        self.__area = pi* radius ** 2
        
    def get_radius(self):
        return self.__radius
    
    def get_diameter(self):
        return self.__diameter
    
    def get_area(self):
        return self.__area
    
    def set_radius(self, new_radius):
        self.__radius = new_radius
        self.__diameter = new_radius * 2
        self.__area = pi* new_radius ** 2

    

    


new_circle = Circle(5)
print(f"Радиус - {new_circle.get_radius()}\nДеаметр - {new_circle.get_diameter()}\nПлощадь - {new_circle.get_area()}")
print(f"Изменим радиус")
print()
new_circle.set_radius(3)
print(f"Радиус - {new_circle.get_radius()}\nДеаметр - {new_circle.get_diameter()}\nПлощадь - {new_circle.get_area()}")
