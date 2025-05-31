dck = {

} 


def create_word():
    engword = input(" enter the English word: ")
    franword = input(" enter the French word: ")
   
    return{"engword": engword, "franword": franword}

def add_word(word: dict):
    id = tuple(word.values())
    dck[id] = word

def del_word(word: dict):
    id = tuple(word.values())
    del dck[id]
    print(f"{word['engword']} {word['franword']} успешно удален из списка")

def find_word(text: str):
    for word in dck.values():
        if text in word.values():
            print(word)
    

def change_word(old_word: dict, new_word: dict):
    del_word(old_word)
    add_word(new_word)
    


print(dck)
pl_1 = create_word()
add_word(pl_1)
print(dck)
add_word(create_word())
print(dck)

# add_word(pl)
# print(dck)
# del_word(pl)
# print(dck)

# find_word()
# print(dck)

