import itertools
from itertools import repeat


def dv(n):
    t = "0123456789ab"
    s = ""
    while  n > 0:
        s = t[n % 12] + s
        n =  n // 12
    return s


def f(n):
    y1 = int(n[0], 12) + int(n[2], 12)
    y2 = int(n[1], 12) + int(n[3], 12)
    m = sorted([y1, y2])
    return dv(m[1]) + dv(m[0])



for x in itertools.product("12456b", repeat = 4):
    if f("".join(x)) == "115":
        print("".join(x))