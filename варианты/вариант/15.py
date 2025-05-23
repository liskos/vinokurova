for a in range(0, 1000):
    if all( not((x&52 != 0)and (x&48 == 0)) or not(x& a == 0) for x in range(0, 1000)):
        print(a)
        break