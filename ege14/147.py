def f(n):
    s = ''
    while n >0:
        s = str(n%7) + s
        n = n//7
    return s

s = 49**12- 7**10 +7**8-49
r = f(s)
print(r.count("6"))