a = [int(x) for x in open("17.txt")]
b = len([x for x in a if len(str(x)) == 2])
r =  []
for i in range(0, len(a)- 1):
    if a[i] % 10 + a[i+1] % 10 == b:
        r.append(a[i] + a[i+1])
print(len(r), min(r))
