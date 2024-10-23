s = set()
for i in range(20, 600):
    b = bin(i)[2:]
    b = b[:-2]
    r = int(b, 2)
    s.add(r)
print(len(s))