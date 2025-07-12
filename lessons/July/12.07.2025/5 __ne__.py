class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, value):
        if isinstance(value, Point):
            return self.x == value.x and self.y == value.y
        else:
            False


    def __ne__(self, value): # определяет неравенство как True только булевые значения
        return True


    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
dot1 = Point(2,3)
dot2 = Point(2,3)  
dot3 = Point(4,3)  
print(dot1 == dot2)  
print(dot2 == dot3)  

print(dot1 != dot2)  
print(dot2 != dot3)  
