for a in range(1, 100):
    if all((x&57 == 0) or ((x&23 != 0) or (x & a != 0)) for x in range(1, 100)):
        print(a)
        break
        