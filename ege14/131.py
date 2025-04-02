for x in range(10, 1000):
    for y in range(0, 1000):
        if str(hex(x))[-2] == "8" and str(hex(x))[-3] == "1" and str(oct(y))[-3] == "7" and str(oct(y))[-2] == "2" and len(oct(y)[2:]) == 3 and len(hex(x)[2:]) == 3:
            print(x, y)
            break