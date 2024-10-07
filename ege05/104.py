def f(n):
    y1 = n % 4
    y2 = n % 3
    y3 = n % 2
    return str(y1) + str(y2) + str(y3)

print(f(55))
for i in range(10, 100):
    if f(i) == '220':
        print(i)
