def f(n):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + ("1")
        else:
            b = b + "0"
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + ("1")
        else:
            b = b + "0"
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + ("1")
        else:
            b = b + "0"
    return int(b, 2)

a = set()
for i in range(1, 1000):
    if i > 95 and f(i) % 4 == 0:
        a.add(i)
print(min(a))