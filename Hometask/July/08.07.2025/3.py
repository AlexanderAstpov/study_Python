def remove_vowels(s:str):
    vowels = ["а", "я", "у", "ю", "о", "ё", "э", "е", "и", "ы"]
    
    result = "".join(ch for ch in s if ch.lower() not in vowels)
    return result
    
s = "программирование"
print(remove_vowels(s))
        

