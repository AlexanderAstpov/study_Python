# перехват ошибок

try:
    dct = {
        [1,2,2]: "start",
    }
    print(int("a"))
    print(1/0)

except Exception as e:
    print(type(e).__name__)
    print(e)