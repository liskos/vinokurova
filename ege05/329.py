def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + "010"
    else:
        b = b + str(bin((n%3)*5)[2:])
    return int(b, 2)

print(f(13))
for i in range(1, 1000):
    if f(i) > 300 and f(i) % 2 == 0:
        print(i, f(i))