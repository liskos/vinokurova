def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = b[1:]
    else:
        b = b.replace("0","") + "1"
    if b.count("1") % 2 == 0:
        b = b[1:]
    else:
        b = b.replace("0","") + "1"
    return int(b, 2)

print(f(5))
k = 0
for i in range(1, 1001):
    if f(i) == 7:
        k += 1
print(k)