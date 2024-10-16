def f(n):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b +'1'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b +'1'
    return int(b, 2)

k = 0
for i in range(1, 1000):
    if f(i) >= 16 and f(i) <= 32:
        k += 1
print(17 - k)
