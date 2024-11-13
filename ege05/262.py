def f(n):
    if n % 2 == 0:
        n1 = n // 2
    else:
        n1 = n - 1
    if n1 % 3 == 0:
        n2 = n1 // 3
    else:
        n2 = n1 - 1
    if n2 % 5 == 0:
        n3 = n2 // 5
    else:
        n3 = n2 - 1
    return n3

s = set()
for i in range(2, 1000):
    if f(i) == 3:
        s.add(i)
print(len(s))
