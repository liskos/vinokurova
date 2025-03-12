def f(n):
    oc = oct(n)[2:]
    if n % 2 == 0:
        oc = oc.replace("1", "2")
        oc = oc.replace("3", "2")
        oc = oc.replace("5", "2")
        oc = oc.replace("7", "2")
    else:
        oc = oc.replace(oc[0], "3").replace(oc[-1], "3")
    return int(oc, 8)

a = set()
print(f(9), f(12))
for i in range(1, 1000):
    if f(i) < 300:
        a.add(f(i))
print(max(a))
