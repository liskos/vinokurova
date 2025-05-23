def f(n):
    b = bin(n)[2:]
    b = b + str(b.count("1")% 2)
    b = b + str(b.count("1") % 2)
    return int(b, 2)

print(f(12) == 48, f(7) == 30)
a = set()
for i in range(1, 10000):
    if f(i) > 253:
        a.add(i)
print(min(a))
    