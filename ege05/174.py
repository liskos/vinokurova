def f(n):
    b = bin(n)[2:]
    b = b.replace("0", '')
    return int(b, 2)

s = set()
for i in range(10,2500):
    s.add(f(i))
print(len(s))