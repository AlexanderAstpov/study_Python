import random as r

print(r.random())
 
# for i in range(5):
#     print(r.random())


# for i in range(5):
#     print(r.randrange(2, 100, 2))

# for i in range(5):
#     print(r.randint(10, 100)) # генерирует в полном диапозоне

lst = [i for i in range(10)]
print(r.choice(lst))

print(r.sample(lst,4))