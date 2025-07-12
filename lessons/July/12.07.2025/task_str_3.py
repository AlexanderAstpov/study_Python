class Book:
    def __init__(self, name, auter, year):
        self.name = name
        self.auter = auter
        self.year = year
        
    def __str__(self):
        return f'"{self.name}", {self.auter}, {self.year}'


burateno = Book("Буратино","Алексей Николаевич Толстой", "1899")

print(burateno)