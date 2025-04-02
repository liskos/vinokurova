def f(n):
    s = ''
    while n >0:
        s = str(n%3) + s
        n = n//3
    return s

s = 2*27**7+3**10-9
r = f(s)
print(r.count("0"))