def f(n):
    b = bin(n)[2:]
    if int(b, 2) % 2 == 0:
        b = b + "1"
    else:
        b = b +"0"
    if int(b, 2) % 2 == 0:
        b = b + "1"
    else:
        b = b + "0"
    return int(b, 2)

print(f(9))
for i in range(1, 1000):
    if f(i) < 171:
        print(i)
