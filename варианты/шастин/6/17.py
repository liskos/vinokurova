a = [int(x) for x in open("17.txt")]
m = min(a)
r = []
for i in range(len(a)-2):
    k1 = [x for x in a[i:i+3] if x > 0]
    k2 = [x for x in a[i:i+3] if x < 0]
    if len(k2) > len(k1) and abs(sum(a[i:i+3])) % 10 == abs(m) % 10:
        r.append(abs(sum(a[i:i+3])))
print(len(r), max(r))
