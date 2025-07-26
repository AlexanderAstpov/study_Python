from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = pi* radius ** 2

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius 
        else:
            return False
        
    def __gt__(self, other):
        if isinstance(other, Circle):
            self.area > other.area
            return True
        else:
            return False
        
    def __iadd__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        

A1 = Circle(5)
A2 = Circle(4)
print(A1 == A2)
A1 += Circle(2)
print(A1.radius)