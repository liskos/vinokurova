def f(n):
    b = bin(n)[2:].zfill(8)
    b = b[:-1]
    b = b[::-1]
    return int(b, 2)


for i in range(1, 100):
    if f(i) == i:
        print(i)