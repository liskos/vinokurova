for a in range(0, 10000):
    if all(((x<7) or (y >= 5*x + a - 60) or (x >= 36) or y<225) for x in range(7, 36) for y in range(225, 1000)):
        print(a)