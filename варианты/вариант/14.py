s = 7**350 + 7**150
for x in range(1, 2300+1):
    s1 = s - x
    k = 0
    while s1 > 0:
        if s1% 7 == 0:
            k += 1
        s1 = s1// 7
    if k == 200:
        print(x)
