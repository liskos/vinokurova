for a in range(1, 1000):
    if all(not((x % 10 != 5) and (x % 10 == 4)) or (x > a - 11) for x in range(1000)):
        print(a)