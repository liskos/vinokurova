a = [int(i) for i in open("17.txt")]
b = [i for i in a if len(str(i)) == 3 and str(i)[-2:] == "33"]
p = []
for i in range(len(a)-2):
    t = a[i:i+3]
    t1 = [i for i in t if len(str(abs(i))) == 5 and str(i)[-2:] == "61"]
    if len(t1) >= 1 and (t[0]+t[1]+t[2]) >= max(b):
        p.append(t[0]+t[1]+t[2])
print(len(t), max(t))
