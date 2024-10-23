def f(n):
    b = bin(n)[2:]
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    return int(b, 2) + n

a = []
for i in range(1, 1000):
    if f(i) <= 123:
        a.append(i)
print(max(a))


