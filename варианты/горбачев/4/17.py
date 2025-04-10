a = [int(i) for i in open("17.txt")]
c = [i for i in a if abs(i)%2 == 0]
r = []
for i in range(0, len(a)-1):
    if (a[i] < 0 and a[i+1] <0) or (a[i] >0 and a[i+1] > 0) and abs(a[i]- a[i+1]) <= len(c):
        r.append(a[i] +a[i+1])
print(len(r), max(r))