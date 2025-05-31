numbers = [1000, 5, 23, 456]
numbers.sort(key=lambda x: len(str(x)))
print(numbers)