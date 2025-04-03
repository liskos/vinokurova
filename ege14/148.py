def f(n):
    s = ''
    while n >0:
        s = str(n%3) + s
        n = n//3
    return s

s = 27**4 - 9**5 + 3**8 -25
r = f(s)
print(r.count("2"))