def sh(n):
    s = ""
    while n > 0:
        s = str(n % 6) + s
        n = n // 6
    return s

def f(n):
    x = sh(n)
    x = x[::-1]
    x = x + x[-1]
    x = int(x, 6)
    x2 = bin(x)[2:]
    x2 = x2 + x2[-1]
    return int(x2, 2)


a = []
for i in range(1, 1000):
    if f(i) < 344:
        a.append(f(i))
print(max(a))
