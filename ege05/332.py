def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + "0"
    else:
        b = b + "1"
    if bin(n)[2:].count("1") % 2 == 0:
        b = b + "0"
    else:
        b = b + "1"
    return int(b, 2)

print(f(13))
for i in range(1, 1000):
    if f(i) > 2023:
        print(f(i))
        break