class MagicItem:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level


    def __str__(self):
        return f"Магический предмет: {self.name}"
    
    def __repr__(self):
        return f"MagicItem('{self.name}', {self.power_level})"
    
    def __lt__(self, other):
        if isinstance(other, MagicItem):
            return (self.name, self.power_level) < (other.name, other.power_level)
        return True

    
    def __eq__(self, value):
        if isinstance(value, MagicItem):
            return (self.name, self.power_level) == (value.name, value.power_level)
        return True
    
item1 = MagicItem("Fire Wand", 5)
item2 = MagicItem("Ice Wand", 7)
item3 = MagicItem("Fire Wand", 5)  

print(item1 < item2) 
print(item1 == item3) 
print(str(item1)) 
print(repr(item2)) 