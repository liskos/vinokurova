def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + str(b[-3:])
    else:
        b = b +str(bin((n%3)*3)[2:])
    return int(b, 2)

print(f(4))
for i in range(1, 1000):
    if f(i) >= 120:
        print(i)
        break