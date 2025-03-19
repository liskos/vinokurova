import sys
sys.setrecursionlimit(5000)

def f(n):
    if n == 3:
        return 3
    elif n > 3:
        return (3+n) * f(n-1)

