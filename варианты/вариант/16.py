def f(n):
    if n >= 2025:
        return n
    else:
        return n *2 + f(n+2)

print(f(82)- f(81))