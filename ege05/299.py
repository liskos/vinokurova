def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = b[1:]
        while b[0] == "0":
            b = b[1:]
    else:
        b =  "1" + b + "00"
    if b.count("1") % 2 == 0:
        b = b[1:]
        while b[0] == "0":
            b = b[1:]
    else:
        b = "1" + b + "00"
    return int(b, 2)

print(f(5))
a = set()
for i in range(1, 1001):
    if f(i) > 100:
        a.add(i)
print(min(a))