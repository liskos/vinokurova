a = [int(line) for line in open("17.txt")]
b = [i for i in a if str(i)[-1] == "7"]
c = []
for i in range(len(a)-1):
    if a[i] * a[i+1] < 0 and a[i] + a[i+1] < len(b):
        c.append(a[i] + a[i+1])
print(len(c), max(c))
