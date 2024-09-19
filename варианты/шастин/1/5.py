def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = b + "11"
    else:
        b = "01" + b
    return int(b, 2)


a = []
for i in range(1, 1000):
    if f(i) > 61:
        a.append(f(i))
print(min(a))