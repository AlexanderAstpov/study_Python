class House:
    def __init__(self):
        self.color = ""
        self.rooms = 0
    
    def count_rooms(self):
        self.rooms += 1
        return self.rooms

    def change_color(self, color):
        self.color = color
        return self.color


my_house = House()
print(my_house.change_color("red"))
print(my_house.count_rooms())
print(my_house.count_rooms())
print(my_house.count_rooms())


        
    