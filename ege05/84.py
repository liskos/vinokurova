def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + "1"
    else:
        b = b + "0"
    b = b + "(b.count("1") % 2)"
    return int(b, 2)


a = []
for i in range(1, 1000):
    if f(i) > 31:
        a.append(f(i))
print(min(a))
