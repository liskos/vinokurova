def f(n):
    s = sum(map(int, str(n)))
    b = bin(s)[2:]
    if b.count("1") % 2 == 0:
        b = "1" + b + "00"
    else:
        b = "10" + b+ "1"
    return int(b, 2)

print(f(123456789))
a = set()
for i in range(100000000, 1000000000):
    if f(i) == 21:
        a.add(i)
print(len(a))