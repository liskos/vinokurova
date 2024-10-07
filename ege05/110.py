def f(n):
    y1 = n % 2
    y2 = n % 3
    y3 = n % 5
    return str(y1) + str(y2) + str(y3)

print(f(55))
k = 0
for i in range(10, 100):
    if f(i) == '122':
        k += 1
print(k)

