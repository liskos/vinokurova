def f(n):
    s = ''
    while n >0:
        s = str(n%5) + s
        n = n//5
    return s

s = 4*25**4-5**4+14
r = f(s)
print(sum(map(int, str(r))))
print(r)