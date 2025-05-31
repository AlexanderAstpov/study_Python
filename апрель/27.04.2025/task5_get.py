# подсчитать повторяюшиеся символы в строке
s = input("введите любой текст: ")
dct ={}

for ch in s.split(): # убрать split и будет считаль по символам
    dct[ch] = dct.get(ch, 0) + 1
    
print(dct)
