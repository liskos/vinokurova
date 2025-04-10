for x in range(0, 17):
    s = int("95790", 17) + x + int("30108", 17) + x*17**3
    if s%11 == 0:
        print(s//11)