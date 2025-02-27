def chet(n):
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        s = str(n%4) + s
        n = n//4
    return s

def f(n):
    cht = chet(n)
    if sum(map(int,cht)) % 2 == 0:
        cht = "31" + cht + "02"
    else:
        cht = "1" + cht + str(chet((n % 3) * 7))
    return int(cht, 4)

print(f(11), f(12))
a = set()
for i in range(1, 1000):
    if f(i) < 4528:
        a.add(i)
print(max(a))








