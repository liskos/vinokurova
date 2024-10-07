def f(n):
    y1 = n % 7
    y2 = n % 2
    y3 = n % 5
    return str(y1) + str(y2) + str(y3)

print(f(55))
k = 0
for i in range(10, 100):
    if f(i) == '312':
        k += 1
print(k)

