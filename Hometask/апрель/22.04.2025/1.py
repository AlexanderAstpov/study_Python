words = ["яблоко", "груша", "апельсин", "киви"]
words.sort(key=lambda x: len(x), reverse=True)
print(words)