import sys
sys.setrecursionlimit(20000)

def f(n):
    if n < 100:
        return n*n
    elif n > 99 and n%2 == 0:
        return 0,5 * f(n-1)
    else:
        return 2* f(n-1)

print(1000 * (f(16384)//f(7777)))