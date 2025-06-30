s = open("1.txt", "w", encoding="utf-8")

s.write("Добрый вечер господа и дамы")
try:
    print(s.read())
    s.close()
    print("file is closed")
except Exception as e:
    print(e)
finally:
    s.close()
    print("file is closed")