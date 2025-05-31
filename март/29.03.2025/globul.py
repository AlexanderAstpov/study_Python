peoples = 20
# peoples = 102

def print_Pposad():
    # peoples = 80
    print(f"Численность населения в ПП {peoples} тысяч человек")

def print_Noginsk():
    # global peoples - позволяет перезаписать глобальныю переменныю из функции
    peoples = 102

    print(f"Численность населения в ногинск {peoples} тысяч человек") 

# def print_Noginsk(peoples):
#     # global peoples - позволяет перезаписать глобальныю переменныю из функции
#     peoples = 102

#     print(f"Численность населения в ногинск {peoples} тысяч человек") 


print(peoples)
print_Pposad()
print_Noginsk()
print(peoples)
# print_Noginsk(peoples)
