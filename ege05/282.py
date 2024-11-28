def f(n):
    b = bin(n)[2:]
    s = sum(map(int, str(b)))
    if n % 2 == 0:
        b = b + bin(s)[2:]
    else:
        b = "1" + b + "00"
    return int(b, 2)


a = set()
for i in range(1, 1000):
    if f(i) > 215:
        a.add(i)
print(min(a))