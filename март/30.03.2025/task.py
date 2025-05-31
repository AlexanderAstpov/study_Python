# функция которая находит гиппотенузу
def find_hypotenuse(a, b):
    hypot = (a**2 + b**2) ** 0.5
    return hypot

a = find_hypotenuse(3, 4)
# print(find_hypotenuse(3, 4))
print(a)
