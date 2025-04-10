import sys
sys.setrecursionlimit(70000)

def f(n):
    if n<100:
        return n
    else:
        return n + f(n-2)

print(f(66666)/f(777))