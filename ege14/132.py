for x in range(10, 1000):
    for y in range(10, 1000):
        if str(hex(x))[-2] == "4" and str(hex(x))[-3] == "3" and str(oct(y))[2] == "1" and str(oct(y))[-3] == "6" and len(oct(y)[2:]) == 4 and len(hex(x)[2:]) == 3:
            print(x, y)
            break