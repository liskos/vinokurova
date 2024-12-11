def f(n):
    b = bin(n)[2:]
    if n % 4 == 0:
        b = b + str(b[-2:])
    else:
        b = str(bin((n%4)*2)[2:]) + b
    return int(b, 2)

print(f(10))
for i in range(4, 1000):
    if f(i) < 168:
        print(i)