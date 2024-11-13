def f(n):
    b = bin(n)[2:]
    if b.count("0") > 0:
        bf0 = b[:b.rfind("0")]
        af0= b[b.rfind("0"):]
        b = bf0 + b[0] + b[1] + af0
    b = b[::-1]
    return int(b, 2)


a = set()
for i in range(2, 1000):
    if f(i) == 119:
        a.add(i)
print(max(a))