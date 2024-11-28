def ch(n):
    t = "0123"
    s = ""
    while  n > 0:
        s = t[n % 4] + s
        n =  n // 4
    return s

def f(n):
    x = ch(n)
    x = str(n % 2) + x + str(n % 3)
    return int(x, 4)

print(f(23))
a = set()
for i in range(1, 1000):
    if 10 <= f(i) < 100:
        a.add(f(i))
print(max(a))


