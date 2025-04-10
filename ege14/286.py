for x in range(1, 1000000):
    s = 4**2015 + 2**x -2**2015 +15
    r = bin(s)[2:]
    if r.count("1") == 500:
        print(x)