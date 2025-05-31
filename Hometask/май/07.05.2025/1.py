d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

d1 |= d2
print(d1)

def merge_two_dicts(x, y):
    z = x.copy()  
    z.update(y)    
    return z

z = merge_two_dicts(d1, d2)
print(z)