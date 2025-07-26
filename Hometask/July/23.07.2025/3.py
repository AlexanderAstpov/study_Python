class Airplane:
    def __init__(self, type_of, num_of_pass, max_pas):
        self.type_of = type_of
        self.num_of_pass = num_of_pass
        self.max_pas = max_pas


    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type_of == other.type_of 
        else:
            return True
        
    def __iadd__(self, other):
        if isinstance(other, Airplane):
            self.num_of_pass += other.num_of_pass
            return (self.num_of_pass)
          
            
        
    def __isub__(self, other):
        if isinstance(other, Airplane):
            self.real -= other.real
            return Airplane(self.real)     
        
    
    def __ge__(self, other):
        if isinstance(other, Airplane):
            self.max_pas >= other.max_pas
            return True
        
    def __le__(self, other):
        if isinstance(other, Airplane):
            self.max_pas <= other.max_pas
            return True
        

    def __str__(self):
        if self.max_pas < self.num_of_pass:
            return f"{self.num_of_pass}"
        else:
            print("превышенно")   
        

a1 = Airplane("A", 200, 450)
a2 = Airplane("B", 350, 350)


print(a1 == a2)
print(a1 >= a2)
a1+= a2
print(a1)



