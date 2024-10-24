
a = [int(x)for x in open("17.txt")]
m = min([x for x in a if x > 0 and str(x)[-1] == "4"])

r =  []
for i in range(len(a) - 2):
    if sum(map(int, str(abs(a[i])))) + sum(map(int, str(abs(a[i+1])))) + sum(map(int, str(abs(a[i+2])))) == m:
        r.append(a[i] +a[i+1]+ a[i+2])
print(len(r),max(r))
