import sys
sys.setrecursionlimit(5000)

def f(n):
    if n == 2070:
        return 5
    if n > 5:
        return 5 * n * f(n-1)
print(5*2075*5*2076*(5*2077/36-1))

