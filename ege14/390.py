for x in range(0,8):
    s1 = int("57A09", 16) +x*16
    s2 = int("540", 8) +x
    s = s1*s2
    n = []
    while s > 0:
        n.append(s%12)
        s = s//12
    if sum(n) == 40:
        print(s1*s2)