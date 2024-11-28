def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = b[:-4] + b[-4:].replace("1", "2").replace("0", "1").replace("2", "0")
    else:
        b = b[:-5] + b[-5:-1].replace("1", "2").replace("0", "1").replace("2", "0") + b[-1]
    return int(b, 2)

print(f(36))
a = set()
mr = 1000
r = 0
for i in range(64, 1000):
    if f(i) < mr :
        mr = f(i)
        r = i

print(r)
