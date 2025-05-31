def hello():
    print("Hello World!")

# hello()

def new_ability(func):
    def wrapper():
        print("Фунционал перед функцией")
        func()
        print("Фунционал после функциии")
    return wrapper

# new_ability(hello)

hello = new_ability(hello)
hello()

