import sys
sys.setrecursionlimit(10000)

def f(n):
    if n <= 10:
        return 10
    else:
        return 7 * n * f(n-2)

print((9242* 7 *19) - (f(9241) * 19/f(9240)))
