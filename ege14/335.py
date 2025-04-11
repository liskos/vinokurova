a = set()
for x in range(0, 5000):
    n = 3*16**2018-2*8**1028 - 3*4**1100 - 4**x - 2022
    s = 0
    if n <0:
        break
    while n > 0:
        s += n%4
        n = n//4
    a.add(s)
print(a)