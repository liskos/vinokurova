def f(n):
    b = bin(n)[2:]
    s = sum(map(int, str(b)))
    if n % 2 == 0:
        b = b + bin(s)[2:]
    else:
        b = "1" + b + "00"
    return int(b, 2)


a = set()
for i in range(1, 10000):
    if f(i) < 1000:
        a.add(i)
print(max(a))