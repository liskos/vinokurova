def tr(n):
    s = ""
    while n > 0:
        s = str(n% 3) + s
        n = n //3
    return s

def f(n):
    t = tr(n)
    if n % 3 == 0:
        t = t + t[-2:]
    else:
        t = t + tr((n%3)*3)
    return int(t, 3)

print(f(6), f(4))
a = set()
for i in range(1, 1000):
    if f(i) <= 150:
        a.add(i)
print(max(a))