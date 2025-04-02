def f(n):
    s = ''
    while n >0:
        s = str(n%4) + s
        n = n//4
    return s

s = 3*16**8 - 4**5 +3
r = f(s)
print(r.count("3"))