class Shape:
    def __init__(self):
        pass


class Rectandle(Shape):
    pass

class Triangle(Shape):
    pass


class Circle(Shape):
    pass

class Square(Rectandle):
    pass

class Iso_triangle(Triangle):
    pass

class Equ_triangle(Triangle):
    pass


print(issubclass(Square, Rectandle)) # являеься ли класс наследником 
print(issubclass(Iso_triangle,Triangle)) # являеься ли класс наследником 