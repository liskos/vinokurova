def f(n):
    b1 = bin(n)[2:]
    b2 = str(b1) + str(b1[-1:])
    if b1.count('1') % 2 == 0:
        b2 = b2 + "0"
    else:
        b2 = b2 + "1"
    if b2.count('1') % 2 == 0:
        b2 = b2 + "0"
    else:
        b2 = b2 + "1"
    return int(b2, 2)


for i in range(1, 1000):
    if f(i) > 80:
        print(f(i))
        break