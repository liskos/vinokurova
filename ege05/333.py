def tr(n):
    s = ""
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s

def f(n):
    n3 = tr(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2] + n3[-1]
    else:
        n3 = n3 + tr((n%3)* 5)
    return int(n3, 3)

print(f(11))
a = set()
for i in range(1, 1000):
    if f(i) > 133:
        a.add(f(i))
print(min(a))