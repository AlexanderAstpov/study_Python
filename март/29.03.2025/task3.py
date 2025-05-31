def draw_line(len_line, derection, symbol):
    if derection == 'vertical':
        print(f"{symbol}\n" * len_line)

    elif derection == 'horizontal':
        print(symbol * len_line)

    else:
        print('Wrong direction')

draw_line(10, "vertical", "%")
draw_line(10, "horizontal", "%")