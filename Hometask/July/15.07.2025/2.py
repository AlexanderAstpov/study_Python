class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__genre =genre
        self.__author = author
        self.__price = price


    @property
    def name(self):
        return self.__name
    

    @property
    def year(self):
        return self.__year
    
    @property
    def publisher(self):
        return self.__publisher
    
    @property
    def genre(self):
        return self.__genre
    
    @property
    def author(self):
        return self.__author
    
    @property
    def price(self):
        return self.__price
    


    @name.setter
    def name(self, new_name):
        self.__name = new_name
    

    @year.setter
    def year(self, new_year):
        self.__year = new_year
    
    @publisher.setter
    def publisher(self, new_publisher):
        self.__publisher = new_publisher
    
    @genre.setter
    def genre(self, new_genre):
        self.__genre = new_genre
    
    @author.setter
    def author(self, new_author):
        self.__author = new_author
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    


        

Akunin = Book("Azazel", "1998", "life", "Historical detective", "Akunin", 450)
print(Akunin.genre)
print()
 
Akunin.name = " Турецкий гамбит"
Akunin.year = 2005
Akunin.publisher = "life"
Akunin.genre = "Historical detective"
Akunin.author = "Akunin"
Akunin.price = 500

print(f"Название - {Akunin.name}\nГод печати - {Akunin.year}\nТипография - {Akunin.publisher}\nЖанр - {Akunin.genre}\nАвтор - {Akunin.author}\nЦена - {Akunin.price}")