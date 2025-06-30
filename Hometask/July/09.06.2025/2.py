class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre =genre
        self.author = author
        self.price = price
        

Akunin = Book("Azazel", "1998", "life", "Historical detective", "Akunin", 450)
print(Akunin.genre)