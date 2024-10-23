def f(n):
    b = bin(n)[2:].zfill(8)
    b = b[:2] + b[-2:]
    return int(b, 2)


for i in range(1, 110):
    if f(i) == 7:
        print(i)

