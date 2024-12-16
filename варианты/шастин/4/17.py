a = [int(x) for x in open("17.txt")]
m = max(a) % 10
s = []
for i in range(0, len(a)-1):
    if (i + 1 + i + 2) % 10 == m:
        s.append(abs(a[i] + a[i+1] - (i+ 1 + i + 2)))
print(len(s), min(s))
