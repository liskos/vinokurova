for x in range(0, 17):
    s = int("13101", 15) + x*15 + int("1303", 17) + x*17
    if s%11== 0:
        print(s//11)