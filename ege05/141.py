def f(n):
    b = bin(n)[2:]

    b = str(b) + str(b[-1:])
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    return int(b, 2)



for i in range(1, 1000):
    if f(i) > 130:
        print(i)
        break