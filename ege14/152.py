def f(n):
    s = ''
    while n >0:
        s = str(n%5) + s
        n = n//5
    return s

s = 4*125**4-25**4+9
r = f(s)
print(r.count("4"))