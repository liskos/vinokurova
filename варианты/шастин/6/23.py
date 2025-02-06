def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*2, b) + f(a*3, b)

print(f(10, 30)* f(30,70))
print(f(10, 60)* f(60,70))
print(f(10, 30)* f(30,60)*f(60, 70))
print(56-16+71-16)