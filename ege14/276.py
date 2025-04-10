def f(n):
    t = "0123456789№#@$*"
    s = ""
    while n > 0:
        s = t[n%15] + s
        n = n//15
    return s

s = 100**2+625**25+5**100
r = f(s)
print(r.count("@"))