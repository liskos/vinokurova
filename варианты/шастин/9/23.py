def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a-3, b) + f(a//2, b)

print(f(69, 14))
print(f(69, 26) * f(26, 14))
print(f(69, 30) * f(30, 14))
