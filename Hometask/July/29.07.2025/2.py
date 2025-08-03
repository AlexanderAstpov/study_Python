class Ship:
    def __init__(self,name, length, width):
        self.name = name
        self.length = length
        self.width = width
        print(f"Название - {self.name}, Длина - {self.length}, Ширина - {self.width}, Скорость - {self.speed}")  
        

class Frigate(Ship):
    def __init__(self, name, length, width, speed):
        self.speed = speed
        super().__init__(name, length, width)

    def _frigate(self):
        print("Современные фрегаты - это высокотехнологичные и многофункциональные боевые корабли,\nспособные выполнять широкий спектр задач в открытом море, что делает их важным элементом военно-морских сил многих стран. ")
        print()

class Destroyer(Ship):
    def __init__(self, name, length, width, speed):
        self.speed = speed
        super().__init__(name, length, width)

    def _destroyer(self):
        print("Эсминец — это быстрый, маневренный, долговечный военный корабль,\nпредназначенный для сопровождения более крупных судов в составе флота, конвоя или авианосной боевой группы и их защиты от широкого спектра общих угроз")   
        print()

class Cruiser(Ship):
    def __init__(self, name, length, width, speed):
        self.speed = speed
        super().__init__(name, length, width)

    def _cruiser(self):
        print("Современные крейсеры, как правило, являются крупными и мощными кораблями,\nспособными решать широкий спектр боевых задач в составе флота и самостоятельно, в том числе,\nобеспечивать противовоздушную оборону, наносить удары по наземным и морским целям,\nа также выполнять разведывательные и патрульные функции")

a1 = Frigate("Фригат", 150, 15, 30)
a1._frigate()
d = Destroyer("Эсминец", 50, 5.8, 19)
d._destroyer()
c = Cruiser("Крейсер", 250, 30, 33)
c._cruiser()

