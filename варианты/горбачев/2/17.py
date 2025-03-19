a = [int(line) for line in open("17.txt")]
b = [i for i in a if i < 0 and abs(i) % 5 == 0]
p = []
for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = [i for i in t if len(str(abs(i))) == 4]
    if len(t1) >= 2 and (t[0] + t[1] + t[2]) >= len(b):
        p.append(t[0]+t[1]+t[2])
print(len(p), min(p))
