for a in range(1, 100):
    if all(((x < a+2) and (y < a-3) and (3*x + y > 66)) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)