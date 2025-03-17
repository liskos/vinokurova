a = [int(line) for line in open("17.txt")]
b = [i for i in a if len(str(abs(i))) == 4]
s = sum(b)
p = []
for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = [i for i in t if len(str(abs(i))) == 3]
    if len(t1) == 2 and t[0] * t[1] * t[2] > s:
        p.append(t[0] *t[1] * t[2])
print(len(p), abs(min(p)))