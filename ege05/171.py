def f(n):
    b = bin(n)[2:].zfill(8)
    b = b[:2] + b[-2:]
    return int(b, 2)

for i in range(130, 256):
    if f(i) == 10:
        print(i)

