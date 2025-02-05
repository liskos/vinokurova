def chet(n):
    s = ""
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s

def f(n):
    cht = chet(n)
    if n % 4 == 0:
        cht = "2" + cht + "03"
    else:
        cht = cht + str(chet((n % 4)* 5))
    return int(cht, 4)

print(f(11))
a = set()
for i in range(1, 1000):
    if f(i) <= 567:
        a.add(i)
print(max(a))
