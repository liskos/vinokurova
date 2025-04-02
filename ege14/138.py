def f(n):
    s = ''
    while n > 0:
        s = str(n%8)+s
        n = n //8
    return s

s = 2**1024 + 2**1026
r = f(s)
print(len(r))