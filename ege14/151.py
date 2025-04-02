def f(n):
    s = ''
    while n >0:
        s = str(n%6) + s
        n = n//6
    return s

s = 5 * 36**7 + 6**10 -36
r = f(s)
print(r.count("5"))