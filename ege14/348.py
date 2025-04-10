for x in range(0, 18):
    s = int("90090", 18) + x + int("22570", 18) + x
    if s%15 == 0:
        print(s//15)