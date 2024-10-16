def f(n):
    b = bin(n)[2:]
    if sum(map(int, str(b))) % 2 == 0:
        b = b + '1'
    else:
        b = b + '0'
    if sum(map(int, str(b))) % 2 == 0:
        b = b + ''
    else:
        b = b + '0'
    return int(b, 2)

k = 0
for i in range(1, 1000):
    if f(i) <= 32 and f(i) >= 16:
        k += 1
print(k)