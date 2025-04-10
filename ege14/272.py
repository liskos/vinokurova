from itertools import count


def f(n):
    t = "0123456789abcdef"  # например 12ca3 - число которое надо перевести
    s = ""
    while n > 0:
        s = t[n % 16] + s
        n = n // 16
    return s

s = 15+2**10+16
r = f(s)
print(r.count("f"))