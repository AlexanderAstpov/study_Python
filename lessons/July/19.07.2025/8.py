class Triangle:
    def __init__(self, b, a, c):
        self.a = a
        self.b = b
        self.c = c


    @property
    def perimetr(self):
        return self.a + self.b + self.c
    
class Equ_triangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


f1 = Triangle(2,6, 3)
f2 = Equ_triangle(6)

print(f1.perimetr)
print(f2.perimetr)
