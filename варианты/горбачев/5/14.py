def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n = n // 7
    return s

k = 0
for x in range(1, 1000+1):
    n = 5**x +31**31 -46**17 - x
    if f(n).count("6") > 100 and f(n).count("6") < 1000:
        k+= 1
print(k)
