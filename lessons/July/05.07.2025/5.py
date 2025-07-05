class Gun:
    def __init__(self):
        self.count = 3


    def shoot(self):
        if self.count <= 0:
            print("перезаряди")
        else:
            if self.count % 2 == 0:
                print("Пиф")
            else:
                print("Паф")
            self.count -= 1
        
       
    def shoot_count(self):
        return self.count
    
    def reload(self):
        self.count = 30
       

my_gun = Gun()
my_gun.shoot()
my_gun.shoot()
my_gun.shoot()
my_gun.shoot()
print(my_gun.shoot_count())
