class Complex:
    def __init__(self, real):
        self.real = real
        

    def __iadd__(self, other):
        if isinstance(other, Complex):
            self.real += other.real
            return Complex(self.real)
             
        
    def __isub__(self, other):
        if isinstance(other, Complex):
            self.real -= other.real
            return Complex(self.real)  

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(complex(self.real / other.real))
        
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(complex(self.real * other.real))    

    def __str__(self):
        return f"{complex(self.real)}"    


a = Complex(2)
b = Complex(4)
a+= b
b-= a
v = b/a
q = a * b

print(a)
print(b)
print(v)
print(q)






