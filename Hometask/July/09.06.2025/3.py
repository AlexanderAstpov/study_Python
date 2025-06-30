class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity
        

Moscow = Stadium("Moscow", "2000", "Russia", "Moscow", 50000)
print(Moscow.capacity)