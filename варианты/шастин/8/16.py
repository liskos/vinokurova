def f(n):
    if n < 15:
        return 4
    elif n >= 15 and n%3 == 0:
        return f(2*n/3) + n - 1
    else:
        return f(n-1)+3

a = set()
for i in range(1, 1000000):
    if f(i) == 251:
        a.add(i)
print(max(a))