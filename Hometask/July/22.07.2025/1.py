class ColorRGB:
    def __init__(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.r = r
            self.g = g
            self.b = b
        else:
            self.r = 0
            self.g = 0
            self.b = 0
            print("Ошибка заданных значений")

       
    
    def __str__(self):
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"
    
    def __repr__(self):
        return f"ColorRGB({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, ColorRGB):
            return (self.r, self.g, self.b) == (other.r, other.g, other.b)
        return False
    
color1 = ColorRGB(255, 0, 0)
color2 = ColorRGB(255, 0, 0)
color3 = ColorRGB(0, 255, 0)

print(color1)
print(repr(color1))
print(color1 == color2)