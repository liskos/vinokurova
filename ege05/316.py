def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + str(b[-3:])
    else:
        b = b + str(bin((n%5)*5)[2:])
    return int(b, 2)

print(f(10))
for i in range(4, 1000):
    if f(i) < 100:
        print(i)