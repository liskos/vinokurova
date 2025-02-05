a = [int(x) for x in open("17.txt")]
m = min([x for x in a if abs(x) % 10 == 7])
s = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    p = [x for x in t if len(str(abs(x))) == 5]
    if len(p) >= 1 and (t[0] * t[1] * t[2]) % abs(m) == 0:
        s.append(t[0] * t[1] * t[2])
print(len(s), max(s))