class Hero:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    @property
    def health(self):
         return self.__health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    @property
    def is_alive(self):
        if self.__health > 0:
            return True
        else:
            return False

    def take_damage(self, damage):
            new_health = self.__health - damage
            print(f"Герой {self.name} получил {damage} урона, осталось: {new_health} здоровья")
            self.health = new_health
            
    def __str__(self):
        return f"Герой {self.name}, Здоровье: {self.health}"
    
         


hero1 = Hero("Арагорн", 100)
hero1.take_damage(25)

print(hero1) 
    
hero2 = Hero("Гэндальф", 120)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")
hero2.health = 50 
print(hero2)

hero2.take_damage(150) 
print(hero2)
print(f"Жив ли {hero2.name}? {hero2.is_alive}")
