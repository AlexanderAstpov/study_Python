class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        print("Пиф")
        self.count += 1
           
        
    def shoot_count(self):
        return self.count
    

my_gun = Gun()
my_gun.shoot()
my_gun.shoot()
my_gun.shoot()
print(my_gun.shoot_count())


    