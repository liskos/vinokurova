def tr(n):
    s = ""
    while n > 0:
        s = str(n%3) + s
        n = n//3
    return s

def f(n):
    if n % 2 == 0:
        n3 = tr(n) + str(tr(n)[-2:])
    else:
        n3 = tr(n) + str(tr(sum(map(int, str(tr(n))))))
    return int(n3, 3)

print(f(10))
mr = 1000

for i in range(10, 1000):
    if f(i) < mr:
        print(i, f(i))