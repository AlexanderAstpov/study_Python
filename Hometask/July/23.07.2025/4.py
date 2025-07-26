class Flat:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost
        


    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area 
        else:
            return True
        
    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area 
        else:
            return True
    
    
    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.cost >= other.cost
        else:    
            return True
        
    def __le__(self, other):
        if isinstance(other, Flat):
            return self.cost <= other.cost
        else:    
            return True
        
        

    def __str__(self):
        return f"{self.area}"
    

a1 = Flat(110, 6_000_000)
a2 = Flat(100, 5_000_000)

print(a1 == a2)
print(a1 != a2)
print(a1 >= a2)
print(a1 <= a2)

        
        





