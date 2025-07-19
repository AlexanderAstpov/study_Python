class Rectangle:
    def __init__(self, height, width):
        self.width = width
        self.height = height


    @property
    def perimetr(self):
        return (self.height + self.width) *2
    
class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


f1 = Rectangle(2,6)
f2 = Square(6)

print(f1.perimetr)
print(f2.perimetr)
