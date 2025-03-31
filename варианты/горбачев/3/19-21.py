def f(x):
    return x- 11, x//3

a = [" "] * 5000
for i in range(5000):
    if i <= 90:
        a[i] = "0"

for i in range(5000):
    if a[i] == " " and  any(a[x] == "0" for x in f(i)):
        a[i] = "1"

for i in range(5000):
    if a[i] == " " and all(a[x] == "1" for x in f(i)):
        a[i] = "2"

for i in range(5000):
    if a[i] == " " and any(a[x] == "2" for x in f(i)):
        a[i] = "3"

for i in range(5000):
    if a[i] == " " and all(a[x]  in "13" for x in f(i)):
        a[i] = "4"

print(max([s  for s in range(5000) if any(a[x] == "1" for x in f(s))]))
print([i for i in range(5000) if a[i] == "1"])
print([i for i in range(5000) if a[i] == "2"])
print([i for i in range(5000) if a[i] == "3"])
print([i for i in range(5000) if a[i] == "4"])