def f(n, m):
    bn = bin(n)[2:]
    bm = bin(m)[2:]
    sn = sum(map(int, str(bn))) ** 2
    sm = sum(map(int, str(bm))) ** 2
    return sn-sm

print(f(15, 21))
a = set()
for i in range(1, 1000):
    for s in range(1, 1000):
        if f(i,s) == 33:
            a.add(i + s)
print(min(a))
