def f(a,b):
    if a == b:
        return 1
    if a > b :
        return 0
    if a == 23 or a == 50 or a == 51:
        return 0
    return f(a+3, b)+ f(a+4, b)+ f(a*2, b)

print(f(11, 54))
print(720 + 861+ 1075 + 594+4)