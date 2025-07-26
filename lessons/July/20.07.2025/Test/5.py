class Hero:
    # names = "Воин"
    # healths = 110

    def __init__(self, name, health):
        self.name = name
        self.__health = health


    def __eq__(self, other):
        if isinstance (other, Hero):
            return self.__health == other.__health
        else:
            return False
    
    def __lt__(self, other):
        if isinstance (other, Hero):
            return self.__health < other.__health
        return True
    
    def __gt__(self, other):
        if isinstance (other, Hero):
            return self.__health > other.__health
        return True

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
    
    @staticmethod
    def show_rules():
        print("Правила игры: побеждает тот, кто остался жив.")

    @classmethod
    def create_warrior(cls, names, healths):
        cls.names = names
        cls.healths = healths
        return(f"Герой {cls.names}, Здоровье: {cls.healths}")    

    @classmethod
    def create_mage(cls, names, healths):
        cls.names = names
        cls.healths = healths
        return(f"Герой {cls.names}, Здоровье: {cls.healths}")    


    

Hero.show_rules()
warrior = Hero.create_warrior("Воин", 110)
mage = Hero.create_mage("Маг", 80)


print(warrior)
print(mage)