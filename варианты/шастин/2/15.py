
m = range(32,68+1)
n = range(54, 76+1)
d = 100
x1 = 0
x2 = 0


for a1 in range(0, 100):
    for a2 in range(a1, 100):
        a = range(a1, a2+1)
        if all((not ((x in m) or ( x in n)))  == (not (x in a)) for x in range(0, 100)):
            if a2 - a1 < d:
                d = a2 - a1
                x1 = a1
                x2 = a2
print(x1, x2, d)

