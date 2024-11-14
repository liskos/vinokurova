def f(n):
    if n % 3 == 0:
        n1 = n // 3
    else:
        n1 = n - 1
    if n1 % 7 == 0:
        n2 = n1 // 7
    else:
        n2 = n1 - 1
    if n2 % 11 == 0:
        n3 = n2 // 11
    else:
        n3 = n2 - 1
    return n3

s = set()
for i in range(2, 1500):
    if f(i) == 6:
        s.add(i)
        print(i)
print(len(s))
