def f(n):
    b = bin(n)[2:]
    if b.count("0") % 2 == 0:
        b = "1" + b + "1"
    else:
        b = "10" + b
    return int(b, 2)

print(f(6))
a = set()
for i in range(1, 1000):
    if f(i) < 100:
        a.add(f(i))
print(a, max(a))
