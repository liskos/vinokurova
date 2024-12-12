def f(n):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = "1" + b + str(b[-2:])
    else:
        b = str(bin(n%5)[2:]) + b
    return int(b, 2)

print(f(13))
for i in range(1, 1000):
    if f(i) <= 223:
        print(f(i))