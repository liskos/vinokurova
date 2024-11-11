def f(n):
    b = bin(n)[2:]
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + "1"
        else:
            b = b + "0"
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + "1"
        else:
            b = b + "0"
    if b.count("1") == b.count("0"):
        b = str(b) + str(b[-1])
    else:
        if b.count("1") < b.count("0"):
            b = b + "1"
        else:
            b = b + "0"
    return int(b, 2)


print(f(13))
a = set()
for i in range(500):
    if f(i) % 4 == 0 and f(i) % 8 != 0:
        a.add(i)
print(max(a))