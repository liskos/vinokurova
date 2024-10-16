def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + "01"
    else:
        b = b + "10"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 81:
        print(f(i))
        break