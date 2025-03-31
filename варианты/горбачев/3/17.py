a = [int(i) for i in open("17.txt")]
rez = []
for i in range(len(a) -2):
    t = a[i:i+3]
    d = [x for x in t if x % 11 == 0 and abs(x)% 10 == 3]
    if len(d) == 2:
        rez.append(sum(t) *2)
print(len(rez), min(rez))