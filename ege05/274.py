def f(n):
    a = [int(d) for d in str(n)]
    s1 = sum(d for d in a if d%2 == 0)
    s2 = 0
    for j in range(len(a)):
        if (j+1)% 2 != 0:
         s2 += a[j]
    return abs(s1 - s2)

print(f(1234))
for i in range(1, 1000000000):
    if f(i) == 28:
        print(i)
        break
