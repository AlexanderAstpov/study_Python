class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__fullname = surname + " " + name

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_fullname(self):
        return self.__fullname

    def set_newname(self, new_name):
        self.__name = new_name
        self.__fullname = self.__name +" "+ self.__surname

    def set_newsurname(self, new_surname):
        self.__surname = new_surname
        self.__fullname = self.__name + " "+ self.__surname

       

   


my = Person("Александр", "Астапов")
print(my.get_fullname())
my.set_newname("Виталик")
my.set_newsurname("Денисов")

print(my.get_fullname())

