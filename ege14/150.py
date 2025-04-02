def f(n):
    s = ''
    while n >0:
        s = str(n%3) + s
        n = n//3
    return s

s = 2*9**10 - 3**5 +5
r = f(s)
print(r.count("2"))