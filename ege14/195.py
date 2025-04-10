for n in range(5, 30):
    for x in range(2, 100):
        if x**2 - int("30", n) * x + int("240", n) == 0:
            print(x, n)