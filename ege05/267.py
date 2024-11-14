def f(n):
    b = bin(n)[2:]
    b1 = b[0]
    b2 = b[1:]
    b2 = b2.replace("1", "2")
    b2 = b2.replace("0", "1")
    b2 = b2.replace("2", "0")
    b = str(b1) + str(b2)
    return int(b, 2) + n

a = set()
for i in range(1, 1000):
    if i % 2 != 0 and f(i) > 99:
        a.add(i)
print(min(a))
