def find_hypotenuse(a, b):
    hypot = (a**2 + b**2) ** 0.5
    return hypot 

def find_distance(x1, y1, x2, y2):
    distance = find_hypotenuse(x1 - x2, y1 -y2)
    return distance


a = find_distance(2,2,4,4)
print(a)

