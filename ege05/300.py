def f(n):
    b = bin(n)[2:]
    b = b[1:]
    if b.count("1") % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "0"
    return int(b, 2)

print(f(4))
a = set()
for i in range(2, 1000):
    if f(i) < 450:
        a.add(i)
print(max(a))