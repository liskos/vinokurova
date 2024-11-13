def f(n):
    b = bin(n)[2:]
    b2 = str(b) + str(b.count("1") % 2)
    if b.count("1") > b.count("0"):
        b2 = b2 + "0"
    else:
        b2 = b2 + "1"
    return int(b2, 2)

a = set()
for i in range(2, 1000):
    if 50 <= f(i) <= 80:
        a.add(f(i))
        print(f(i))
print(len(a))
