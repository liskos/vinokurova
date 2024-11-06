def f(n):
    b = bin(n)[2:]
    b = str(b) + str(b[-2])
    b = str(b) +str(b[1])
    return int(b, 2)

print(f(11))
a = 0
for i in range(2, 10000):
    if 150 <= f(i) <= 200:
        a += 1
        print(i)
print(a)