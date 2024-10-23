for i in range(500, 10000):
    b = bin(i)[2:]
    b = b[::-1]
    b = b[b.find("1"):]
    if int(b, 2) == 19:
        print(i)
        break