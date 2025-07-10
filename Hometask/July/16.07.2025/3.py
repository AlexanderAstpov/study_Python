
class Rectangle:
    def __init__(self, w, h):
        self.__width = w
        self.__height = h
    

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self.__width = new_width
        else:
            print("Значение должно быть положительным")

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_heidht):
        if new_heidht >= 0:
            self.__height = new_heidht
        else:
            print("Значение должно быть положительным")

    @property
    def area(self):
        self.__area = self.__width * self.__height
        return self.__area
    
    @property    
    def perimeter(self):
        self.__perimeter = (self.__width + self.__height) * 2
        return self.__perimeter

        
    
r = Rectangle(3, 4)
print(r.area) 
print(r.perimeter) 
r.width = -5 
r.height = 10
print(r.area)     