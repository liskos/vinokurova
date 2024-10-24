s = set()
for i in range(20, 601):
    b = bin(i)[2:-2]
    r = int(b, 2)
    s.add(r)
print(len(s))