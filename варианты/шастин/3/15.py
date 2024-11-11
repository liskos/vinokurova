for a in range(1, 1000):
    if all(not((x%7 != 0) and (x % 13 == 0)) or(x > a - 40) for x in range(1, 1000)):
        print(a)