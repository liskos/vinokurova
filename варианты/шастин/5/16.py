import sys
sys.setrecursionlimit(5000)

def f(n):
    if n > 3000:
        return n
    elif n <= 3000:
        return (2*n+4) * f(n+2)

print(f(20)//f(28))