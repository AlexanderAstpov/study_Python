class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
            self.health = self.health - damage
            print(f"Герой {self.name} получил {damage} урона, осталось: {self.health} здоровья")
            
    def __str__(self):
        return f"Герой {self.name}, Здоровье: {self.health}"
    
         


hero1 = Hero("Арагорн", 100)
hero1.take_damage(25)

print(hero1)
    
