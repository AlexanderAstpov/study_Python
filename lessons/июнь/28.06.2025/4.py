def safe_div(a,b):
    try:
        k = a/b
        return k
    except ZeroDivisionError: 
        return "На ноль делить нельзя"

print(safe_div(2,0))
print(safe_div(2,6))