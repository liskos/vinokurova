def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b + "00"
    else:
        b = b + str(bin(sum(map(int, str(b))))[2:])
    return int(b, 2)

print(f(4))
for i in range(9, 1000):
    if f(i) > 88:
        print(i)
        break