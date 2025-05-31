def new_ability(func):
    def wrapper():
        print("Фунционал перед функцией")
        func()
        print("Фунционал после функциии")
    return wrapper

# new_ability(hello)
@new_ability
def hello():
    print("Hello World!")

hello()




