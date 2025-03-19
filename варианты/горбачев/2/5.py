def dev(n):
    s = ""
    while n > 0:
        s = str(n%9) + s
        n = n // 9
    return s

def f(n):
    d = dev(n)
    if sum(map(int, d)) % 2 == 0:
        d = d + "52"
    else:
        d = "73" + d[2:] + "44"
    return int(d, 9)

print(f(11))
a = set()

for i in range(1, 10000):
    if f(i) > 13950:
        a.add(i)
print(min(a))